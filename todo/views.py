from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import NewTaskForm


# Create your views here.
def home(request):
    return render_to_response(
        'home.html',
        {
            'new_task_form': NewTaskForm()
        },
        RequestContext(request)
    )
