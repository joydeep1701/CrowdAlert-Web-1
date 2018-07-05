from rest_framework import permissions

# https://stackoverflow.com/a/49626193
class FirebasePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        The request is authenticated as a user, or is a read-only request.

        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            # Make sure email is verified
            if (
                request.user and
                request.user.get('email', False) and 
                request.user.get('email_verified', False)
            ):
                return True
            return False

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True