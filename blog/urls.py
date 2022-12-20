from .views import UserViewSet, AccountViewSet, OrderViewSet, SnippetDetail, CreateItem
from rest_framework import routers
from django.urls import path

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('scores/<int:pk>/',SnippetDetail.as_view()),
    path('scores2/',SnippetDetail.as_view() ),
    path('product/',CreateItem.as_view() )
]
urlpatterns += router.urls