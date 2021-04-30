from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import TextInput

from .models import ToDo


class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['todo', 'description', 'important']
        widgets = {
            'todo': TextInput(attrs={'autofocus': 'autofocus', 'placeholder': 'Tarefa'}),
            'description': TextInput(attrs={'placeholder': 'Descrição'}),
        }
