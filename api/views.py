from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .permissions import IsOwnerOrReadOnly
from .permissions import IsOwnerOnly
from .serializers import ToDoSerializer
from .serializers import UserSerializer
from todo.models import ToDo


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'users': reverse('api:user-list', request=request, format=format),
        'todos': reverse('api:todo-list', request=request, format=format)
    })


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all().order_by('-created_at')
    serializer_class = ToDoSerializer
    permission_classes = [IsOwnerOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        _queryset = self.queryset.filter(user=self.request.user)
        return _queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ToDoDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = ToDoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
