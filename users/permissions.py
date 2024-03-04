from rest_framework import permissions

class IsAdminOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin or the user itself
        return request.user.is_staff or (obj == request.user)