from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.core import serializers
from django.contrib.auth import authenticate, login as login_user
from .forms import NewTaskForm, LoginForm
from .models import Task


# Create your views here.
def home(request):
    tasks = Task.objects.all().order_by('-id').filter(completed=False)
    completed_tasks = Task.objects.all().order_by('-id').filter(completed=True)
    user = request.user
    return render_to_response(
        'home.html',
        {
            'new_task_form': NewTaskForm(),
            'login_form': LoginForm(),
            'tasks': tasks,
            'completed_tasks': completed_tasks,
            'user': user
        },
        RequestContext(request)
    )


def add_task(request):
    """ given a request with a decription and a valid user, insert
    a new database record representing a task and return a json object
    representing the newly inserted record """
    user = request.user
    description = request.POST.get('description')
    new_task = Task(owner=user, description=description)
    new_task.save()
    return HttpResponse(serializers.serialize('json', [new_task]))


def complete_task(request):
    """ given a request with a task, set the task to completed in the database
    and return a json object representing the newly updated record """
    task_id = request.POST.get('task_id')
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return HttpResponse(serializers.serialize('json', [task]))


def uncomplete_task(request):
    """ given a request with a task, set the task to not completed in the
    database and return a json object representing the newly updated record """
    task_id = request.POST.get('task_id')
    task = Task.objects.get(pk=task_id)
    task.completed = False
    task.save()
    return HttpResponse(serializers.serialize('json', [task]))


def delete_task(request):
    """ given a request with a task, delete the task """
    task_id = request.POST.get('task_id')
    task = Task.objects.get(pk=task_id)
    task.delete()
    return HttpResponse(serializers.serialize('json', [task]))


def edit_task(request):
    """ given a request with a task, set the task description in the database and return a json object representing the newly updated record """
    task_id = request.POST.get('task_id')
    description = request.POST.get('description')
    task = Task.objects.get(pk=task_id)
    task.description = description
    task.save()
    return HttpResponse(serializers.serialize('json', [task]))


def login(request):
    """ given a username and a password, log the user in and return them to the
    todo page """
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login_user(request, user)
    return redirect(home)
