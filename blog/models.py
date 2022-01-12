import uuid
from django.db import models

# Create your models here.
class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=30)
    date = models.DateTimeField()
    url = models.TextField()
    title = models.CharField(max_length=140)
    text = models.TextField()


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=8)
    admin = models.BooleanField(default=False)
