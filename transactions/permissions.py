from rest_framework.permissions import BasePermission

class ExpenseDetailAuthorizationPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        print('from permission:', obj.personRef)
        if request.user == obj.personRef:
            return True
        
        return False