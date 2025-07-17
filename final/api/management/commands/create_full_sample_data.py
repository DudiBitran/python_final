from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import UserProfile, Post, Comment, Tag

class Command(BaseCommand):
    help = 'Create all sample data: users, passwords, profiles, tags, articles, comments.'

    def handle(self, *args, **options):
        self.stdout.write('Creating full sample data...')

        # 1. Create users (superusers and regular)
        users_data = [
            {'username': 'adminuser', 'email': 'adminuser@example.com', 'password': 'AdminPass123', 'is_staff': True, 'is_superuser': True, 'bio': 'Adminuser profile'},
            {'username': 'admin', 'email': 'admin@example.com', 'password': 'AdminPass123', 'is_staff': True, 'is_superuser': True, 'bio': 'Admin profile'},
            {'username': 'user1', 'email': 'user1@example.com', 'password': 'UserPass123', 'is_staff': False, 'is_superuser': False, 'bio': 'User1 profile'},
            {'username': 'user2', 'email': 'user2@example.com', 'password': 'UserPass123', 'is_staff': False, 'is_superuser': False, 'bio': 'User2 profile'},
            {'username': 'john_doe', 'email': 'john@example.com', 'password': 'UserPass123', 'is_staff': False, 'is_superuser': False, 'bio': 'Tech journalist and AI enthusiast.'},
            {'username': 'jane_smith', 'email': 'jane@example.com', 'password': 'UserPass123', 'is_staff': False, 'is_superuser': False, 'bio': 'Environmental activist and writer.'},
            {'username': 'mike_wilson', 'email': 'mike@example.com', 'password': 'UserPass123', 'is_staff': False, 'is_superuser': False, 'bio': 'Health coach and nutrition expert.'},
        ]
        user_objs = {}
        for u in users_data:
            user, created = User.objects.get_or_create(
                username=u['username'],
                defaults={'email': u['email'], 'is_staff': u['is_staff'], 'is_superuser': u['is_superuser']}
            )
            user.set_password(u['password'])
            user.is_staff = u['is_staff']
            user.is_superuser = u['is_superuser']
            user.save()
            user_objs[u['username']] = user
            profile, _ = UserProfile.objects.get_or_create(user=user, defaults={'bio': u['bio']})
            self.stdout.write(f"✅ User: {u['username']} (superuser: {u['is_superuser']})")

        # 2. Create tags
        tag_names = [
            'Technology', 'AI', 'Trends', 'Environment', 'Climate', 'Action', 'Health', 'Nutrition', 'Lifestyle',
            'Work', 'Travel', 'Programming', 'Python', 'Data Science', 'Wellness', 'Business', 'Marketing', 'Finance', 'Investing'
        ]
        tag_objs = {}
        for tag_name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_objs[tag_name] = tag
            self.stdout.write(f'✅ Tag: {tag_name}')

        # 3. Create 10 articles by adminuser and admin
        posts_data = [
            {
                'title': 'The Rise of Artificial Intelligence',
                'text': 'AI is transforming industries and daily life. This article explores the latest trends and applications of AI.',
                'author_username': 'adminuser',
                'tags': ['Technology', 'AI', 'Trends'],
                'status': 'published'
            },
            {
                'title': 'Climate Change: What Can We Do?',
                'text': 'Climate change is one of the biggest challenges of our time. Here are practical steps individuals and communities can take.',
                'author_username': 'admin',
                'tags': ['Environment', 'Climate', 'Action'],
                'status': 'published'
            },
            {
                'title': 'Healthy Eating for Busy People',
                'text': 'Maintaining a healthy diet can be tough with a busy schedule. Here are tips and quick recipes for nutritious meals.',
                'author_username': 'adminuser',
                'tags': ['Health', 'Nutrition', 'Lifestyle'],
                'status': 'published'
            },
            {
                'title': 'The Future of Remote Work',
                'text': 'Remote work is here to stay. Explore the benefits, challenges, and best practices for working from home.',
                'author_username': 'admin',
                'tags': ['Technology', 'Work', 'Trends'],
                'status': 'published'
            },
            {
                'title': 'Traveling on a Budget',
                'text': 'Discover how to see the world without breaking the bank. Tips for affordable travel and hidden gems.',
                'author_username': 'adminuser',
                'tags': ['Travel', 'Lifestyle'],
                'status': 'published'
            },
            {
                'title': 'Mastering Python for Data Science',
                'text': 'Python is the go-to language for data science. Learn the essential libraries and techniques.',
                'author_username': 'admin',
                'tags': ['Programming', 'Python', 'Data Science'],
                'status': 'published'
            },
            {
                'title': 'Mindfulness and Meditation',
                'text': 'Improve your mental health with mindfulness and meditation. Simple exercises for daily life.',
                'author_username': 'adminuser',
                'tags': ['Health', 'Wellness'],
                'status': 'published'
            },
            {
                'title': 'Building Your Personal Brand Online',
                'text': 'Tips for creating a strong personal brand on social media and professional networks.',
                'author_username': 'admin',
                'tags': ['Business', 'Marketing', 'Trends'],
                'status': 'published'
            },
            {
                'title': 'A Beginner’s Guide to Investing',
                'text': 'Learn the basics of investing, from stocks to real estate, and how to get started.',
                'author_username': 'adminuser',
                'tags': ['Finance', 'Investing'],
                'status': 'published'
            },
            {
                'title': 'Sustainable Living: Small Changes, Big Impact',
                'text': 'Adopt sustainable habits at home and in your community. Every small change counts.',
                'author_username': 'admin',
                'tags': ['Environment', 'Lifestyle'],
                'status': 'published'
            }
        ]
        post_objs = {}
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
                    for tag_name in post_data['tags']:
                        tag = tag_objs[tag_name]
                        post.tags.add(tag)
                    self.stdout.write(f'✅ Post: {post.title}')
                post_objs[post.title] = post
            except UserProfile.DoesNotExist:
                self.stdout.write(f'User {post_data["author_username"]} not found, skipping post')

        # 4. Create sample comments
        comments_data = [
            {'post_title': 'The Rise of Artificial Intelligence', 'author_username': 'user1', 'text': 'Fascinating read! AI is truly changing the world.'},
            {'post_title': 'The Rise of Artificial Intelligence', 'author_username': 'user2', 'text': 'Great overview of current AI trends.'},
            {'post_title': 'Climate Change: What Can We Do?', 'author_username': 'john_doe', 'text': 'Very informative. Everyone should read this.'},
            {'post_title': 'Healthy Eating for Busy People', 'author_username': 'jane_smith', 'text': 'Loved the quick recipes!'},
            {'post_title': 'The Future of Remote Work', 'author_username': 'mike_wilson', 'text': 'Remote work tips are so useful!'},
            {'post_title': 'Traveling on a Budget', 'author_username': 'user1', 'text': 'Great travel tips!'},
            {'post_title': 'Mastering Python for Data Science', 'author_username': 'user2', 'text': 'Python is awesome for data science.'},
            {'post_title': 'Mindfulness and Meditation', 'author_username': 'john_doe', 'text': 'Mindfulness really helps me focus.'},
            {'post_title': 'Building Your Personal Brand Online', 'author_username': 'jane_smith', 'text': 'Branding is so important these days.'},
            {'post_title': 'A Beginner’s Guide to Investing', 'author_username': 'mike_wilson', 'text': 'Investing basics explained well.'},
            {'post_title': 'Sustainable Living: Small Changes, Big Impact', 'author_username': 'user1', 'text': 'Every small change really does count!'},
        ]
        for comment_data in comments_data:
            try:
                post = post_objs[comment_data['post_title']]
                author = UserProfile.objects.get(user__username=comment_data['author_username'])
                comment, created = Comment.objects.get_or_create(
                    post=post,
                    author=author,
                    text=comment_data['text']
                )
                if created:
                    self.stdout.write(f'✅ Comment on "{post.title}" by {author.user.username}')
            except (KeyError, UserProfile.DoesNotExist):
                self.stdout.write(f'Post or user not found, skipping comment')

        self.stdout.write(self.style.SUCCESS('Full sample data created successfully!')) 