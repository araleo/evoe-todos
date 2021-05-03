from rest_framework import permissions


class IsOwnerOnly(permissions.BasePermission):
    """
    Permissão personalizada para que apenas o 
    proprietário de um objeto possa interagir
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
