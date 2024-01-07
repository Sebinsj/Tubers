from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    fname=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    company=models.CharField(max_length=200)
    subject=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    created_date=models.DateTimeField(blank=True,default=datetime.now)

    def __str__(self):
        return self.email
   