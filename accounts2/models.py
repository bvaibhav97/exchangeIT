from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

gender = [ ('M','male'), ('F','female')

]
#it will change the default manaer 
class User_Manager(BaseUserManager):  

	#below function will throw errors if u set something as requored and not mentioning here
	def create_user(self, email, full_name, password= None, is_active=False,is_staff=False, is_admin=False):
		if not email:
			raise ValueError("chupchap email de !")		
		if not password:
			raise ValueError("chupchap password de !")
		if not full_name:
			raise ValueError("chup chap full name de ")

		user  = self.model( #creating a user object of the model whose manager this class is
				email = self.normalize_email(email)
						  )
		user.staff = is_staff
		user.admin = is_admin
		user.active = is_active
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_staff(self,full_name, email, password=None):
		user = self.create_user(
			email, 
			full_name, 
			password=password,
			
			is_staff = True,
			is_active = True

			)

	def create_superuser(self, email,password=None):
		user = self.create_user(
			email, 
			full_name, 
			password=password,
			is_staff = True,
			is_active = True,
			is_admin = True

			)

	






class Custom_User(AbstractBaseUser):
	full_name= models.CharField(max_length=50)

	email = models.EmailField(max_length=50, unique= True, default="abc@gmail.com")
	active = models.BooleanField(default=False) #active or not
	staff = models.BooleanField(default=False) #staff
	admin = models.BooleanField(default=False) #supersuer

	objects = User_Manager() #signifies obects of this model referes to the objects manager


	USERNAME_FIELD = 'email'
	REQUIRED_FIELD = ['email','password']

	def get_full_name(self):
		return self.email

	def has_perm(self, perm, obj=None):
		# 		"Does the user have a specific permission?"
		return True

	def has_module_perms(self, app_label):
		#"Does the user have permissions to view the app `app_label`?"
		return True

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.active



class central_db(models.Model):
	full_name= models.CharField(max_length=50)
	DOB = models.DateField(default="auto_now=True")
	username = models.CharField(max_length=50)
	number = models.IntegerField(default="8055504914")
	sex = models.BooleanField(default="Male", choices=gender)
	