from django.db import models
from django.core.validators import MinLengthValidator
from .user_profile import UserProfile
from .post import Post

class Comment(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=200, validators=[MinLengthValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reply_to = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text} by {self.author.user.username}' 