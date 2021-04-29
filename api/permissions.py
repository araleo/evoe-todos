from rest_framework import permissions


class IsOwnerOnly(permissions.BasePermission):
    """
    Custom permission to allow only the owner of an
    object to interact with it (view, edit and delete).
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
