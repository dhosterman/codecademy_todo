from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.core import serializers
from .forms import NewTaskForm
from .models import Task


# Create your views here.
def home(request):
    tasks = Task.objects.all().order_by('-id')
    return render_to_response(
        'home.html',
        {
            'new_task_form': NewTaskForm(),
            'tasks': tasks
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
