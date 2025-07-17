from django.core.management.base import BaseCommand
from api.models import Comment

class Command(BaseCommand):
    help = 'Delete all comments with a null author (orphaned comments)'

    def handle(self, *args, **options):
        orphaned = Comment.objects.filter(author__isnull=True)
        count = orphaned.count()
        orphaned.delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {count} orphaned comments.')) 