from django.contrib.auth.models import User
from django.db import models


class ToDo(models.Model):
    todo = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.todo} de {self.user}'

    @property
    def is_completed(self):
        return bool(self.completed_at)

    @property
    def is_deleted(self):
        return bool(self.deleted_at)

    @property
    def e_importante(self):
        return 'Sim' if self.important else 'Não'
