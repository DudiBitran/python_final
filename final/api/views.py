from rest_framework.viewsets import ModelViewSet
from .serializers import (UserSerializer, PostSerializer, UserProfileSerializer, 
                          CommentSerializer, TagSerializer, PostUserLikeSerializer)

from .models import Tag, UserProfile, Post, Comment, PostUserLikes

class UserViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

 

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

 

class PostUserLikesViewSet(ModelViewSet):
    queryset = PostUserLikes.objects.all()
    serializer_class = PostUserLikeSerializer

 

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
 

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer