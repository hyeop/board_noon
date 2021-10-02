from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    comment = models.TextField(blank=True)
    point = models.IntegerField(default=0)
    pic = models.ImageField(upload_to="usr/%y/%m", default="none.png")

 