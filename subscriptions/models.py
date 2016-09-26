from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):

    text = models.TextField()
    users = models.ManyToManyField(User, related_name='subscriptions')

    def __str__(self):
        return self.text