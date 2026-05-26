from rest_framework.permissions import BasePermission
from rest_framework.request import Request

class IsAdminOrEditor(BasePermission):
    def has_permission(self, request: Request, view) -> bool:
        return request.user.is_authenticated and request.user.role in ['admin', 'editor']