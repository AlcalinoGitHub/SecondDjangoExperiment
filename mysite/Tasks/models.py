from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.

class Task(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    DueDate = models.DateField()
    Completed = models.BooleanField(default=False)
    Owner = models.ForeignKey(User, on_delete= models.CASCADE)
