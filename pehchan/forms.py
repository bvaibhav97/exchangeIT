from django import forms
from .models import users
from bootstrap_datepicker_plus import DatePickerInput
import random

gender = (
		('F', 'Woman'),
		('M', 'Male'),
		('L', 'Others'),
	) 

class formClass(forms.Form):
	unique_no = random.randrange(00, 1000000, 1)
	name = forms.CharField(widget=forms.TextInput(attrs ={"class":"form-control","placeholder":"enter your name"}))
	email = forms.EmailField(widget=forms.TextInput(attrs ={"class":"form-control","placeholder":"enter your email id"}))
	contact = forms.IntegerField(widget=forms.EmailInput(attrs ={"class":"form-control","placeholder":"enter ph number"}))
	date = forms.DateField(
		widget=DatePickerInput()
	)
	password= forms.CharField(widget=forms.PasswordInput(attrs ={"class":"form-control","placeholder":"enter your password"}))
	gender = forms.ChoiceField(choices=gender, widget=forms.Select(attrs ={"class":"form-control","placeholder":"express your gender"}))
	username= forms.CharField(widget=forms.TextInput(attrs ={"class":"form-control","placeholder":"enter username"}))

	class Meta:
		model = users
		fields = ('email','name','password','username','dob','username' )

class loginForm(forms.Form):
	username= forms.CharField(widget=forms.TextInput(attrs ={"class":"form-control","placeholder":"enter username"}))
	password= forms.CharField(widget=forms.PasswordInput(attrs ={"class":"form-control","placeholder":"enter your password"}))

	class Meta:
		model = users
		fields = ('password','username' )




