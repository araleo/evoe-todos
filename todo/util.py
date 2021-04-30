from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .forms import ToDoForm
from .models import ToDo


def operate_todo(request, todo_id=None, update=False):
    # completar todo
    if 'btncomplete' in request.POST:
        complete_todo(request)

    # deletar todo
    if 'btndelete' in request.POST:
        delete_todo(request)

    # criar ou atualizar
    if 'todo' in request.POST: 
        if update:
            update_todo(request, todo_id)
        else:
            create_todo(request)


def redirect_after_post(request, todo_id=None):
    if todo_id and not 'btndelete' in request.POST:
        return HttpResponseRedirect(f'/todo/{todo_id}')
    return HttpResponseRedirect('/todo')


def get_obj(request, pk):
    return get_object_or_404(ToDo, pk=pk, user=request.user)


def complete_todo(request):
    todo = get_obj(request, request.POST['todo_pk'])
    todo.completed_at = timezone.now()
    todo.save()


def delete_todo(request):
    todo = get_obj(request, request.POST['todo_pk'])
    todo.deleted_at = timezone.now()
    todo.save()


def create_todo(request):
    form = ToDoForm(request.POST)
    if form.is_valid():
        new_todo = form.save(commit=False)
        new_todo.user = request.user
        new_todo.save()


def update_todo(request, todo_id):
    todo = get_obj(request, todo_id)
    form = ToDoForm(request.POST, instance=todo)
    if form.is_valid():
        form.save()
