from datetime import date

from django.core.management.base import BaseCommand

from core.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()

        user = User()
        user.username = 'kowalski'
        user.first_name = 'Jan'
        user.last_name = 'Kowalski'
        user.birthday = date(2000, 1, 1)
        user.save()

        user = User()
        user.username = 'nowak'
        user.first_name = 'Jan'
        user.last_name = 'Nowak'
        user.birthday = date(2008, 5, 4)
        user.save()