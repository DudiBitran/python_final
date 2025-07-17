from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from api.models import Comment, Post, PostUserLikes, Tag, UserProfile
from rest_framework import serializers
from django.core.validators import RegexValidator

class UserSerializer(ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[
                    RegexValidator(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$',
                                    message="Password must contain at least 8 characters, including one uppercase letter, one lowercase letter, and one number."
                       )
                    ]
    )
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
        # extra_kwargs = {'password': {'write_only': True}}
        # fields = '__all__'
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user   
    
    def update(self, instance, validated_data):
   

       
        password = validated_data.pop('password', None)

       
        for key, value in validated_data.items():
            setattr(instance, key, value)


        instance.set_password(password)

        instance.save()

        return instance 

 
class CommentSerializer(ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "author", "created_at", "post"]

    def get_author(self, obj):
        # Return username and id
        if obj.author and hasattr(obj.author, 'user'):
            return {
                "id": obj.author.user.id,
                "username": obj.author.user.username
            }
        return None

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['author'] = request.user.userprofile
        return super().create(validated_data)

 
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