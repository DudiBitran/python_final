from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, PostViewSet, UserProfileViewSet, CommentViewSet, TagViewSet, PostUserLikesViewSet, RegistrationView, ArticleCommentsView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .token_serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', PostViewSet, basename='article')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'tags', TagViewSet)
router.register(r'likes', PostUserLikesViewSet)
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

 

#optional: we can add more patterns here:

urlpatterns += [
    path('articles/<int:article_id>/comments/', ArticleCommentsView.as_view(), name='article-comments'),
]