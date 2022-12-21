from .views import UserViewSet, AccountViewSet, OrderViewSet, SnippetDetail, CreateItem, ExampleView
from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('scores/<int:pk>/',SnippetDetail.as_view()),
    path('scores2/',SnippetDetail.as_view() ),
    path('product/',CreateItem.as_view() ),
    path('session/',ExampleView.as_view() ),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
urlpatterns += router.urls