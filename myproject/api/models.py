from django.db import models

# Create your models here.
class user_details(models.Model):
    userid = models.IntegerField()
    title = models.TextField(max_length=200)
    body = models.CharField(max_length=10)
