from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import random
import datetime


def random_number():
    return random.randint(1, 100)


class UserExtension(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()
    number = models.IntegerField(default=random_number(), unique=True)

    def get_age(self):
        return int(datetime.date.year)-int(self.birthday.year)
