from django.conf.urls import include
from django.urls import path
from s4sbackendapi.views import register_user, login_user
from rest_framework import routers
from s4sbackendapi.views import Samples
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'samples', Samples, 'samples')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)