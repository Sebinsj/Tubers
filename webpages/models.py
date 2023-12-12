from django.db import models

# Create your models here.
class Team(models.Model):
     firstname=models.CharField(max_length=255)
     lastname=models.CharField(max_length=255)
     role=models.CharField(max_length=255)
     fb_link=models.CharField(max_length=255)
     linkedin_link=models.CharField(max_length=200,blank=True)
     insta_link=models.CharField(max_length=255)
     photo=models.ImageField(upload_to="media/team/%Y/%m/%d/")
     created_date=models.DateField(auto_now_add=True)

     def __str__(self):
         return self.firstname




class Slider(models.Model):
    headline=models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    button_text=models.CharField(max_length=255)
    photo=models.ImageField(upload_to="media/slider/%Y/")
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.headline 
      

 