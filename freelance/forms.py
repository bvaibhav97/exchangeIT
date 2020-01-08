from django import forms
from .models import freelance_basic
from bootstrap_datepicker_plus import DatePickerInput
 
class free_form(forms.Form):
	Title = forms.CharField(widget=forms.TextInput(attrs ={"class":"form-control","placeholder":"enter your name"}))
	Description = forms.EmailField(widget=forms.TextInput(attrs ={"class":"form-control","placeholder":"enter your email id"}))
	Price = forms.IntegerField(widget=forms.TextInput(attrs ={"class":"form-control","placeholder":"enter ph number"}))

	Date = forms.DateField(
		widget=DatePickerInput()
	)
	

	class Meta:
		model = freelance_basic
		fields = ('Title','Description','Price','Date' )



