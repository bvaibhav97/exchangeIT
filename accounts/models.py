from django.db import models
import random
from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager
	)

class UserManager(BaseUserManager):
	def create_user(self, email, password=None, is_admin= False, active= True, is_staff= False):
		if not email:
			raise ValueError("user must provide an email")
		user_obj = self.Model( #here an object is created which will be used THOUSAND_SEPARATOR = ','initialise things furthur
		email = self.normalize_email(email)

			)
		user_obj.active = active
		user_obj.is_admin = is_admin
		user_obj.is_staff = is_staff

		user-obj.set_password(password)
		user_obj.save(using=self._db)
		return user_obj

	def create_staffuser(self, email, password=None):
		user = create_user(
			email,
			password=password,
			is_staff= True)
		return user 

# Create your models here.

gender = (
        ('F', 'Woman'),
        ('M', 'Male'),
        ('L', 'Others'),
    ) 
abc = int(123)
# Create your :models here.
class Custom_User(AbstractBaseUser):
	email = models.EmailField(max_length= 255, unique=True)
	active = models.BooleanField(default=True)
	admin = models.BooleanField(default=False) #superuser
	DOB = models.DateField(null=True)
	gender = models.CharField(max_length=1,choices=gender)
	timestamd = models.DateTimeField()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS= ['email']

	objects = UserManager()

	def __str__(self):
		return self.full_name

	@property
	def is_admin(self):
		return self.admin
	

class users(models.Model):

    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    DOB = models.DateField(null=True)
         


    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name 
 
  

   