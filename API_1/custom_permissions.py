from rest_framework.permissions import BasePermission



# writting custom permission for get request only
class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True # means user granted
        return False