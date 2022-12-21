from .views import UserViewSet, AccountViewSet, OrderViewSet, SnippetDetail, CreateItem, ExampleView, UpdateItem, snippet_list,snippet_detail
from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('scores/<int:pk>/',SnippetDetail.as_view()),
    path('scores2/',SnippetDetail.as_view(), name = 'game_list' ),
    path('product/',CreateItem.as_view() ),
    path('product/<int:pk>/',UpdateItem.as_view()),
    path('session/',ExampleView.as_view() ),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('snippets/', snippet_list),
    path('snippets/<int:pk>/', snippet_detail),]
#     format_suffix_patterns([
#     path('', views.api_root),
#     path('snippets/',
#         views.SnippetList.as_view(),
#         name='snippet-list'),
#     path('snippets/<int:pk>/',
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'),
#     path('users/',
#         views.UserList.as_view(),
#         name='user-list'),
#     path('users/<int:pk>/',
#         views.UserDetail.as_view(),
#         name='user-detail')
# ])]
urlpatterns += router.urls