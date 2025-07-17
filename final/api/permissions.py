from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit or delete objects.
    """
    def has_permission(self, request, view):
        # SAFE_METHODS are GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admins to delete objects.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Allow authenticated users to POST, everyone else can read.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated 

class IsAdminOrAuthor(permissions.BasePermission):
    """
    Allow admin/superuser or the object's author to edit/delete.
    """
    def has_object_permission(self, request, view, obj):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if user.is_staff or user.is_superuser:
            return True
        # For comments, obj.author is UserProfile, so compare user.id to obj.author.user.id
        return hasattr(obj, 'author') and hasattr(obj.author, 'user') and user.id == obj.author.user.id 