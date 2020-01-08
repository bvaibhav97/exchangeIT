from django.contrib import admin
from django.contrib.auth import get_user_model
from.forms import UserAdminChangeForm, UserAdminCreationForm

Custom_User = get_user_model()

class UserAdmin(admin.ModelAdmin):
	search_fields = ['email']
	form 	 = UserAdminChangeForm
	add_form = UserAdminCreationForm


admin.site.register(Custom_User, UserAdmin)

# Register your models here.
from .models import central_db 

admin.site.register(central_db)		