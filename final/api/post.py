from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from .user_profile import UserProfile
from .tag import Tag

STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('archived', 'Archived')
]

class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, validators=[
        MinLengthValidator(5),
        RegexValidator(regex='^[a-zA-Z].*$')
    ])
    text = models.TextField(validators=[MinLengthValidator(5)])
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return f'{self.title} by {self.author.user.username}' 