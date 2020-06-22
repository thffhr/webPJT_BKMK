from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MaxValueValidator

# Create your models here.

class User(AbstractUser):
    ADULT_CHOICES = (
        ('YES', 'True'),
        ('NO', 'False'),
    )

    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings', blank=True)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    usergenre = models.CharField(max_length=500, default='')
    use_adult = models.CharField(max_length=3, choices=ADULT_CHOICES, default='')