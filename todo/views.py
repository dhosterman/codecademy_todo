from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from .forms import NewTaskForm
from .models import Task


# Create your views here.
def home(request):
    return render_to_response(
        'home.html',
        {
            'new_task_form': NewTaskForm()
        },
        RequestContext(request)
    )


def add_task(request):
    user = request.user
    description = request.POST.get('description')
    new_task = Task(owner=user, description=description)
    new_task.save()
    return redirect(home)
