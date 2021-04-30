from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone

from .forms import ToDoForm
from .models import ToDo
from .util import redirect_after_post
from .util import operate_todo


@login_required
def home(request):
    if request.method == 'POST':
        operate_todo(request)
        return redirect_after_post(request)

    todos = ToDo.objects.filter(user=request.user, deleted_at__isnull=True).order_by('-created_at')
    pending = todos.filter(completed_at__isnull=True)
    completed = todos.filter(completed_at__isnull=False)
    context = {'form': ToDoForm(), 'pending': pending, 'completed': completed}
    return render(request, 'todo/index.html', context)


@login_required
def detail(request, todo_id):
    if request.method == 'POST':
        operate_todo(request, todo_id=todo_id, update=True)
        return redirect_after_post(request, todo_id)        

    todo = get_object_or_404(ToDo, pk=todo_id, user=request.user, deleted_at__isnull=True)
    context = {'todo': todo, 'form': ToDoForm(instance=todo)}
    return render(request, 'todo/detail.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/todo')

    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
