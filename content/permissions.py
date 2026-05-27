from rest_framework.permissions import BasePermission
from rest_framework.request import Request

class IsAdminOrEditor(BasePermission):
    def has_permission(self, request: Request, view) -> bool:
        return request.user.is_authenticated and request.user.role in ['admin', 'editor']
    
class CanPublishArticle(BasePermission):
    def has_permission(self, request: Request, view) -> bool:
        print("\n---> DRF APPELLE CAN_PUBLISH_ARTICLE <---")
        return request.user.is_authenticated and request.user.role in ['admin', 'editor']
    
class CanCreateDraft(BasePermission):
    def has_permission(self, request: Request, view) -> bool:
        print("\n---> DRF APPELLE CAN_CREATE_DRAFT <---")
        return request.user.is_authenticated and request.user.role in ['admin', 'editor', 'author']