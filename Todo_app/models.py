from django.db import models

class Task(models.Model):
    todo = models.CharField(max_length=60)
    completed = models.BooleanField()
    userId = models.IntegerField()
