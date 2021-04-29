from django.contrib.auth.models import User
from rest_framework import serializers

from todo.models import ToDo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail', read_only=True)

    class Meta:
        model = User
        fields = ['username', 'todos']


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ToDo
        fields = ['todo', 'description', 'important', 'user', 'created_at']
