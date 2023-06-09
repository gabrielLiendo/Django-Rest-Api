from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blogs.serializers import BlogViewSet

router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]