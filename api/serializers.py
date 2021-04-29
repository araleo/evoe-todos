from rest_framework import serializers

from todo.models import ToDo


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ToDo
        fields = ['todo', 'description', 'important', 'user', 'created_at']
