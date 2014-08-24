from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User)


# signals
def create_initial_tasks(sender, instance, **kwargs):
    if kwargs['created']:
        task = Task(
            owner=instance,
            description='Hire Daniel (daniel.hosterman@gmail.com) for some work!'
        )
        task.save()

post_save.connect(
    create_initial_tasks,
    sender=User,
    dispatch_uid='create_initial_tasks'
)
