from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):

   SAFE_METHODS = ['HEAD', 'OPTIONS', 'GET', 'PUT', 'DELETE', 'PATCH']

   def has_object_permission(self, request, view, obj):
      if request.user.is_superuser:
         return True
      if request.method in self.SAFE_METHODS:
         return obj.id == request.user.id
      return False

   def has_permission(self, request, view):
      if view.detail:
         return True
      return request.user.is_superuser
