from rest_framework import serializers
from pehchan.models import users

class User_Serializer(serializers.ModelSerializer):
	class Meta:
		model = users
		fields = ['name','email','phone']
