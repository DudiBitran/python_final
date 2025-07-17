from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Set up working passwords for all users'

    def handle(self, *args, **options):
        self.stdout.write('Setting up passwords for users...')
        
        # Define users and their passwords
        users_passwords = {
            'adminuser': 'AdminPass123',
            'user1': 'UserPass123', 
            'user2': 'UserPass123',
            'admin': 'AdminPass123',
            'john_doe': 'UserPass123',
            'jane_smith': 'UserPass123',
            'mike_wilson': 'UserPass123',
        }
        
        for username, password in users_passwords.items():
            try:
                user = User.objects.get(username=username)
                user.set_password(password)
                user.save()
                self.stdout.write(f'✅ Set password for {username}: {password}')
            except User.DoesNotExist:
                self.stdout.write(f'❌ User {username} not found')
        
        self.stdout.write(self.style.SUCCESS('Password setup completed!'))
        self.stdout.write('\nYou can now log in with:')
        self.stdout.write('- adminuser / AdminPass123 (superuser)')
        self.stdout.write('- admin / AdminPass123 (superuser)')
        self.stdout.write('- user1 / UserPass123')
        self.stdout.write('- user2 / UserPass123')
        self.stdout.write('- john_doe / UserPass123')
        self.stdout.write('- jane_smith / UserPass123')
        self.stdout.write('- mike_wilson / UserPass123') 