from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import TextInput

from .models import ToDo


class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['todo', 'description', 'important']
