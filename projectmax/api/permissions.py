from rest_framework.permissions import BasePermission
from .models import Project

class IsOwner(BasePermission):
    """Custom permission is granted to the bucketlist owner."""


    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the project owner."""
        if isinstance(obj, Project):
            return obj.owner == request.user
        return obj.owner == request.user
