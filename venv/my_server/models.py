from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    state = models.CharField(max_length=30, default='')
    name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return 'Username: {username}'.format(username=self.username)

class Entry(models.Model):
    title = models.CharField(max_length=50, default='')
    user_id = models.ForeignKey('MyUser', related_name='user_id', on_delete=models.CASCADE)

    def __str__(self):
        return 'Entry: id = {id}, title = {title}'.format(id=self.id, title=self.title)