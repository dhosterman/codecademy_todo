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


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'})
    )


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'})
    )
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'})
    )
