from rest_framework import routers, permissions
from api import views
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi  # new

router = routers.DefaultRouter()
router.register(r'clubs', views.ClubViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'winners', views.WinnerViewSet)
router.register(r'selections', views.VoteViewSet)
router.register(r'vote', views.VoteViewSet)
vote_list = views.VoteViewSet.as_view({'post': 'post', 'get': 'get'})



urlpatterns = [
    path('', include(router.urls)),
    path('vote/', vote_list, name='vote'),
]