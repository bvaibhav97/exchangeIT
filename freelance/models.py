from django.db import models

# Create your models here.
class freelance_basic(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    Price = models.CharField(max_length=50)
    Date = models.DateField()
         
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name 
 