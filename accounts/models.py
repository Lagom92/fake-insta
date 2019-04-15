from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers", blank=True)
    # 위와 아래는 동일함
    # follow = models.ManyToManyField('self', related_name="follower", blank=True)

    
    def __str__(self):
        return self.username