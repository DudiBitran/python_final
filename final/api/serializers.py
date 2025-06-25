from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from api.models import Comment, Post, PostUserLikes, Tag, UserProfile

 

# from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

 
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

 
class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

 
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

 
class PostUserLikeSerializer(ModelSerializer):
    class Meta:
        model = PostUserLikes
        fields = "__all__"
        # fields = ['text', 'id']