from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'clubs', views.ClubViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'winners', views.WinnerViewSet)
router.register(r'selections', views.SelectionViewSet)
# router.register(r'vote', views.VoteViewSet, basename='vote')
vote_list = views.VoteViewSet.as_view({
    'get': 'list',
    'post': 'update'
})


urlpatterns = [
    path('', include(router.urls)),
    path('vote/', vote_list, name='vote'),
]