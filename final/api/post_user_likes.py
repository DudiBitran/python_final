from django.db import models
from .user_profile import UserProfile
from .post import Post

LIKE_CHOICES = [
    ('like', 'Like'),
    ('dislike', 'Dislike'),
]

class PostUserLikes(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_type = models.CharField(choices=LIKE_CHOICES, default='like')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'post']

    def __str__(self):
        return f'{self.user.user.username} {self.like_type}d {self.post.title}' 