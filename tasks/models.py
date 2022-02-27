from email.policy import default
from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=200, default='None')
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Quote(models.Model):
    quote=models.TextField()
    source = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote
