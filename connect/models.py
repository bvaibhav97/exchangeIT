from django.db import models


# Create your models here.
abc=1

class connect_base(models.Model):
	User_oneId = models.IntegerField(abc)
	User_twoId = models.IntegerField()
	Status 	   = models.IntegerField()
	Action_id  = models.IntegerField()


