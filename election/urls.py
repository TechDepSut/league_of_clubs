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

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@league_of_clubs.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
    permission_classes=(
        permissions.IsAuthenticated,
    ),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
]