from rest_framework.permissions import BasePermission


class IsEnroll(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()
