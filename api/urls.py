from django.urls import path, include
from election.urls import router

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]
