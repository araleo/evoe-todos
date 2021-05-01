from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .permissions import IsOwnerOnly
from .serializers import ToDoSerializer
from todo.models import ToDo


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'todos': reverse('api:todo-list', request=request, format=format)
    })


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all().order_by('-created_at')

    serializer_class = ToDoSerializer
    permission_classes = [IsOwnerOnly]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # filtra apenas os objetos criados pelo usuário
        # e que não tenham o campo deleted_at preenchido
        _queryset = self.queryset.filter(user=self.request.user, deleted_at__isnull=True)
        return _queryset


class ToDoDetail(APIView):
    permission_classes = [IsOwnerOnly]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk):
        obj = get_object_or_404(ToDo, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

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
        todo.deleted_at = timezone.now()
        todo.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
