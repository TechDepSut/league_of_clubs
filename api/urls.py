from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'clubs', views.ClubViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'winners', views.WinnerViewSet)
router.register(r'selections', views.WinnerViewSet)


urlpatterns = [
    path('', include(router.urls)),
]