from django.db import models
import random
gender = (
        ('F', 'Woman'),
        ('M', 'Male'),
        ('L', 'Others'),
    )       
abc = int(123)
# Create your :models here.
class users(models.Model):

    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    password= models.CharField(max_length=50)
    DOB = models.DateField()
    unique_no = models.IntegerField(abc)
         


    sex = models.CharField(max_length=1,choices=gender)
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name 
 
  

   