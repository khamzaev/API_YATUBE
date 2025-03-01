from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet


router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='v1-post')
router_v1.register(r'groups', GroupViewSet, basename='v1-group')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='v1-comment'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
