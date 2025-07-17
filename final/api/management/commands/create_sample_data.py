from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from api.models import UserProfile, Post, Comment, Tag
from datetime import date

class Command(BaseCommand):
    help = 'Create sample data for the blog application'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create tags
        tags = []
        tag_names = ['Technology', 'AI', 'Trends', 'Environment', 'Climate', 'Action', 'Health', 'Nutrition', 'Lifestyle']
        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)
            if created:
                self.stdout.write(f'Created tag: {tag_name}')
        
        # Create additional users if they don't exist
        users_data = [
            {'username': 'john_doe', 'email': 'john@example.com', 'bio': 'Tech journalist and AI enthusiast.'},
            {'username': 'jane_smith', 'email': 'jane@example.com', 'bio': 'Environmental activist and writer.'},
            {'username': 'mike_wilson', 'email': 'mike@example.com', 'bio': 'Health coach and nutrition expert.'},
        ]
        
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={'email': user_data['email']}
            )
            if created:
                user.set_password('password123')
                user.save()
                profile, profile_created = UserProfile.objects.get_or_create(
                    user=user,
                    defaults={'bio': user_data['bio']}
                )
                self.stdout.write(f'Created user: {user.username}')
        
        # Create additional posts (real-world articles)
        posts_data = [
            {
                'title': 'The Rise of Artificial Intelligence',
                'text': 'Artificial Intelligence (AI) is transforming industries and daily life. This article explores the latest trends and applications of AI.',
                'author_username': 'john_doe',
                'tags': ['Technology', 'AI', 'Trends'],
                'status': 'published'
            },
            {
                'title': 'Climate Change: What Can We Do?',
                'text': 'Climate change is one of the biggest challenges of our time. Here are practical steps individuals and communities can take to make a difference.',
                'author_username': 'jane_smith',
                'tags': ['Environment', 'Climate', 'Action'],
                'status': 'published'
            },
            {
                'title': 'Healthy Eating for Busy People',
                'text': 'Maintaining a healthy diet can be tough with a busy schedule. This article provides tips and quick recipes for nutritious meals on the go.',
                'author_username': 'mike_wilson',
                'tags': ['Health', 'Nutrition', 'Lifestyle'],
                'status': 'published'
            }
        ]
        
        for post_data in posts_data:
            try:
                author = UserProfile.objects.get(user__username=post_data['author_username'])
                post, created = Post.objects.get_or_create(
                    title=post_data['title'],
                    defaults={
                        'author': author,
                        'text': post_data['text'],
                        'status': post_data['status']
                    }
                )
                if created:
                    # Add tags
                    for tag_name in post_data['tags']:
                        tag = Tag.objects.get(name=tag_name)
                        post.tags.add(tag)
                    self.stdout.write(f'Created post: {post.title}')
            except UserProfile.DoesNotExist:
                self.stdout.write(f'User {post_data["author_username"]} not found, skipping post')
        
        # Create additional comments (real-world context)
        comments_data = [
            {'post_title': 'The Rise of Artificial Intelligence', 'author_username': 'jane_smith', 'text': 'Fascinating read! AI is truly changing the world.'},
            {'post_title': 'The Rise of Artificial Intelligence', 'author_username': 'mike_wilson', 'text': 'Great overview of current AI trends.'},
            {'post_title': 'Climate Change: What Can We Do?', 'author_username': 'john_doe', 'text': 'Very informative. Everyone should read this.'},
            {'post_title': 'Healthy Eating for Busy People', 'author_username': 'jane_smith', 'text': 'Loved the quick recipes!'},
        ]
        
        for comment_data in comments_data:
            try:
                post = Post.objects.get(title=comment_data['post_title'])
                author = UserProfile.objects.get(user__username=comment_data['author_username'])
                comment, created = Comment.objects.get_or_create(
                    post=post,
                    author=author,
                    text=comment_data['text']
                )
                if created:
                    self.stdout.write(f'Created comment on "{post.title}" by {author.user.username}')
            except (Post.DoesNotExist, UserProfile.DoesNotExist):
                self.stdout.write(f'Post or user not found, skipping comment')
        
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!')) 