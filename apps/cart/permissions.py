from rest_framework import permissions


class IsOwnerCustomer(permissions.BasePermission):
   def has_permission(self, request, view):
      return int(view.kwargs['pk']) == request.user.id
