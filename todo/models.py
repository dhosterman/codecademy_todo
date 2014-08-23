from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User)
