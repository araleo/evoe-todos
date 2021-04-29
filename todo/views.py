from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .forms import ToDoForm
from .models import ToDo


@login_required
def home(request):

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return HttpResponseRedirect('/todo/')

    latest_todos_list = ToDo.objects.order_by('-created_at')[:5]
    context = {
        'form': ToDoForm(),
        'todos': latest_todos_list
    }
    return render(request, 'todo/index.html', context)


def detail(request, todo_id):
    todo = get_object_or_404(ToDo, pk=todo_id)
    return render(request, 'todo/detail.html', {'todo': todo})


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/todo')

    if request.method == 'GET':
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})