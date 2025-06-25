from rest_framework.routers import DefaultRouter
from .views import (CommentViewSet, PostViewSet, PostUserLikesViewSet,
                    UserProfileViewSet, UserViewSet, TagViewSet)

router = DefaultRouter()

router.register('tags', TagViewSet, basename='tags')
router.register('comments', CommentViewSet, basename='comments')
router.register('posts', PostViewSet, basename='posts')
router.register('users', UserViewSet, basename='users')
router.register('userprofiles', UserProfileViewSet, basename='userprofiles')
router.register('likes', PostUserLikesViewSet, basename='likes')

urlpatterns = router.urls

 

#optional: we can add more patterns here:

urlpatterns += [

]