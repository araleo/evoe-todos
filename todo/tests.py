from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import ToDo


class ToDoModelTests(TestCase):

    def test_is_completed(self):
        completed_todo = ToDo(completed_at=timezone.now())
        self.assertIs(completed_todo.is_completed, True)

    def test_not_completed(self):
        not_completed_todo = ToDo(completed_at=None)
        self.assertIs(not_completed_todo.is_completed, False)

    def test_is_deleted(self):
        deleted_todo = ToDo(deleted_at=timezone.now())
        self.assertIs(deleted_todo.is_deleted, True)

    def test_not_delete(self):
        not_delete_todo = ToDo(deleted_at=None)
        self.assertIs(not_delete_todo.is_deleted, False)

    def test_e_importante(self):
        important_todo = ToDo(important=True)
        importante = important_todo.e_importante
        self.assertEqual(importante, 'Sim')

    def test_e_importante(self):
        not_important_todo = ToDo(important=False)
        importante = not_important_todo.e_importante
        self.assertEqual(importante, 'Não')
    

class HomeViewTests(TestCase):

    def _login(self):
        self.user = User.objects.create_user('teste', 'teste@teste.com', 'teste')
        self.client.login(username='teste', password='teste')

    def test_no_todos(self):
        self._login()
        response = self.client.get(reverse('todo:index'))
        self.assertContains(response, 'Sem tarefas pendentes')
        self.assertContains(response, 'Sem tarefas concluídas')

    def test_no_completed_todos(self):
        self._login()
        todo = ToDo.objects.create(todo='teste', user=self.user)
        response = self.client.get(reverse('todo:index'))
        self.assertNotContains(response, 'Sem tarefas pendentes')
        self.assertContains(response, 'Sem tarefas concluídas')

    def test_no_pending_todos(self):
        self._login()
        todo = ToDo.objects.create(todo='teste', user=self.user, completed_at=timezone.now())
        response = self.client.get(reverse('todo:index'))
        self.assertContains(response, 'Sem tarefas pendentes')
        self.assertNotContains(response, 'Sem tarefas concluídas')


class DetailViewTests(TestCase):

    def _login(self):
        self.user = User.objects.create_user('teste', 'teste@teste.com', 'teste')
        self.client.login(username='teste', password='teste')

    def test_detail_page(self):
        self._login()
        todo = ToDo.objects.create(todo='teste', user=self.user)
        response = self.client.get(reverse('todo:detail', kwargs={'todo_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_user(self):
        self._login()
        other_user = User.objects.create_user('teste2', 'teste2@teste.com', 'teste2')
        todo = ToDo.objects.create(todo='teste 2', user=other_user)
        response = self.client.get(reverse('todo:detail', kwargs={'todo_id': 1}))
        self.assertEqual(response.status_code, 404)
