from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class User(AbstractUser):
    ADULT_CHOICES = (
        (True, 'YES'),
        (False, 'NO'),
    )

    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings', blank=True)
    age = models.IntegerField(validators=[MinValueValidator(13), MaxValueValidator(100)], default=13)
    usergenre = models.CharField(max_length=500, default='1')
    use_adult = models.BooleanField(choices=ADULT_CHOICES, default=False)