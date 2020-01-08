from rest_framework import generics
from pehchan.models import users
from .serializers import User_Serializer

class UserListAPIView(generics.ListAPIView):
	 queryset = users.objects.all()
	 serializer_class = User_Serializer


	 def get_queryset(self):
	 	return users.objects.all()


