from django import forms
from todo.models import Task


class NewTaskForm(forms.ModelForm):

    class Meta():
        model = Task
        fields = ['description']
