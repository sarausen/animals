from rest_framework.permissions import BasePermission


class IsAuthenticatedOrSafeMethods(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return True
        else:
            if request.user and request.user.is_authenticated:
                return True
        return False