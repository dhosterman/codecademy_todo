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
                'autofocus': True,
                'required': True
                })
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'required': True})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'required': True})
    )


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'required': True})
    )
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'First Name', 'required': True})
    )
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Last Name', 'required': True})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'required': True})
    )
