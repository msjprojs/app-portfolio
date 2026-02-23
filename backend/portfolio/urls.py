from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet, SkillViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'skills', SkillViewSet, basename='skills')
router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = [
    path('', include(router.urls))
]