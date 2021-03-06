from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.core import serializers
from django.contrib.auth import authenticate, login as login_user, \
    logout as logout_user
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from .forms import NewTaskForm, LoginForm, RegisterForm
from .models import Task


# Create your views here.
def home(request):
    user = request.user
    if user.is_active:
        tasks = Task.objects.all().order_by('-id')\
            .filter(completed=False, owner=user)
        completed_tasks = Task.objects.all().order_by('-id')\
            .filter(completed=True, owner=user)
    else:
        tasks = None
        completed_tasks = None
    return render_to_response(
        'home.html',
        {
            'new_task_form': NewTaskForm(),
            'login_form': LoginForm(),
            'register_form': RegisterForm(),
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
    """ given a request with a task, set the task description in the database
     and return a json object representing the newly updated record """
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
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'User or password are incorrect.'
        )
    return redirect(home)


def logout(request):
    """ logout the user """
    logout_user(request)
    return redirect(home)


def register(request):
    """ register a new user """
    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password = request.POST.get('password')
    try:
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save()
        authenticated = authenticate(username=username, password=password)
        login_user(request, authenticated)
    except IntegrityError:
        messages.add_message(
            request,
            messages.ERROR,
            'This user already exists.'
        )
    return redirect(home)
