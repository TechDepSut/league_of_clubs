from django.urls import path, include
from rest_framework import routers
from .views import ClubViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register(r"clubs", ClubViewSet)
router.register(r"students", StudentViewSet)
