from django.db import models
from datetime import datetime

# Create your models here.
class Hiretuber(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    tuber_id=models.IntegerField()
    tuber_name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    user_id=models.IntegerField(blank=True)
    created_date=models.DateTimeField(blank=True,default=datetime.now)

    def __str__(self):
        return self.email
   