from django import forms
from django.forms import TextInput
from todo.models import Task


class NewTaskForm(forms.ModelForm):

    class Meta():
        model = Task
        fields = ['description']
        widgets = {
            'description': TextInput(attrs={
                'placeholder': 'Enter new task...',
                'autofocus': True
                })
        }
