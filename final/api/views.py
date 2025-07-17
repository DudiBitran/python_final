from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import (UserSerializer, PostSerializer, UserProfileSerializer, 
                          CommentSerializer, TagSerializer, PostUserLikeSerializer)

from .models import Tag, UserProfile, Post, Comment, PostUserLikes
from rest_framework.permissions import AllowAny
from .permissions import IsAdminOrReadOnly, IsAdmin, IsAuthenticatedOrReadOnly, IsAdminOrAuthor
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework import status, filters
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

 

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]

 

class PostUserLikesViewSet(ModelViewSet):
    queryset = PostUserLikes.objects.all()
    serializer_class = PostUserLikeSerializer

 

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text', 'tags__name', 'author__user__username']

    

 

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            permission_classes = [IsAdminOrAuthor]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]


class ArticleCommentsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, article_id):
        comments = Comment.objects.filter(post_id=article_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, article_id):
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            from .models import Post
            post = Post.objects.get(pk=article_id)
            serializer.save(post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)