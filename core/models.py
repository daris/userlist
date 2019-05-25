import random
from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    random_number = models.IntegerField(blank=True, null=True)

    def get_age(self):
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    def save(self, *args, **kwargs):
        if not self.pk:
            self.random_number = random.randint(1, 100)

        super().save(*args, **kwargs)
