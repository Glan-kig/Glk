from django.urls import path, include
from rest_framework import routers
from content.views import PostViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]