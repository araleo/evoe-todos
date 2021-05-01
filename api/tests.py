from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import RequestsClient
from rest_framework.test import force_authenticate

from .views import ToDoDetail


class TestAPIViews(TestCase):

    def test_root(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/')
        self.assertEqual(response.status_code, 200)

    def gen_token(self):
        user = User.objects.create_user('teste', 'teste@teste.com', 'teste')
        data = {'username': 'teste', 'password': 'teste'}
        response = self.client.post('http://127.0.0.1:8000/api/api-token-auth/', data=data)
        self.token = response.json()['token']

    def _login(self):
        self.client = RequestsClient()
        self.gen_token()
        self.headers = {'Authorization': f'Token {self.token}'}

    def test_token(self):
        self._login()
        self.assertIsNotNone(self.token)

    def create_todo(self):
        data = {'todo': 'teste'}
        response = self.client.post('http://127.0.0.1:8000/api/todos/', headers=self.headers, data=data)
        return response

    def test_create_todo(self):
        self._login()
        response = self.create_todo()
        self.assertEqual(response.status_code, 201)

    def test_get_todo(self):
        self._login()
        new_todo = self.create_todo()
        pk = new_todo.json()['id']
        response = self.client.get(f'http://127.0.0.1:8000/api/todos/{pk}/', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_todo(self):
        self._login()
        new_todo = self.create_todo()
        pk = new_todo.json()['id']
        response = self.client.delete(f'http://127.0.0.1:8000/api/todos/{pk}/', headers=self.headers)
        self.assertEqual(response.status_code, 204)

    def test_put_todo(self):
        self._login()
        new_todo = self.create_todo()
        pk = new_todo.json()['id']
        data = {'todo': 'Teste!'}
        response = self.client.put(f'http://127.0.0.1:8000/api/todos/{pk}/', headers=self.headers, data=data)
        self.assertEqual(response.status_code, 200)

    def test_list_todos(self):
        self._login()
        new_todo = self.create_todo()
        response = self.client.get('http://127.0.0.1:8000/api/todos/', headers=self.headers)
        self.assertEqual(response.status_code, 200)
