from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # allowing read-only permission for anyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # allowing write permission only for the author
        return obj.author == request.user