from django.db import models
from django.contrib.auth.models import User


class Subscription(models.Model):

    users = models.ManyToManyField(User, related_name='subscriptions', blank=True)
    full_name = models.TextField(max_length=20)
    short_name = models.TextField(max_length=3, unique=True)

    def __str__(self):
        return self.full_name