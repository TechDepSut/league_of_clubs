from django.urls import path, include
from rest_framework import routers, permissions
from .views import ClubViewSet, StudentViewSet, WinnerViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'clubs', ClubViewSet)
router.register(r'students', StudentViewSet)
router.register(r'winners', WinnerViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path('', include(router.urls)),
]