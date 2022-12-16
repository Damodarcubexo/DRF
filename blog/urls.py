from .views import UserViewSet, AccountViewSet
from rest_framework import routers
from django.urls import path

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)
urlpatterns = []
urlpatterns += router.urls