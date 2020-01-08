from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from .forms import formClass,loginForm
from django.http import HttpResponseRedirect
from .models import users 
from django.views.generic import View 
from django.urls import reverse

class Signup(View):
	model = users 
	
	template_name= "signup.html" 

	def get(self, request, *args, **kwargs ):
		forminstance = formClass(request.GET)	
		context = { 
		'form': forminstance
		}
		return render(request,'signup.html', context)
		...  # code to process a GET request

	def post(self, request, *args, **kwargs ):
		name = 	request.POST.get("username")
		print(name)
		userform = users() #its a great discovery , making an object of the db modeel
		userform.name= name #n literally storing new daya in object
		userform.unique_no = 123
		userform.save() #n saving it permanantly
		return HttpResponseRedirect("") #i didnt knew it was this easy,

		#but very sad i took so much time for this simple !

class Login(View):
	model = users 
	qs= users.objects.all()
	print('hii2')
	if qs:
		print("objects exists")
	else:
		print("dont exists ")

	def get(self, request, *args, **kwargs ):

		forminstance = loginForm()	
		context = { 
		'form': forminstance
		}
		return render(request,'login.html', context)

		...  # code to process a GET request

	def post(self, request, *args, **kwargs ):
		user_name = request.POST.get("username")
		pass_word = request.POST.get("password") 
		print(user_name)
		print(pass_word)
		print(request.user)

		user = authenticate(request, username = user_name, password = pass_word)
		if user:
			print("user exists")
			login(request,user)
			return HttpResponseRedirect(reverse('admin'))
		else:
			print("user does not exists")
			forminstance = loginForm()	
			context = { 
					'form': forminstance
					}
			return render(request, "signup.html",context)

		#qs = users.objects.filter(username= user_name)
		#if qs:
			#if pass_word == qs[0].password:
				#print('welcome')
			#else:
				#print('username/password do not match')
			
		#else:
			#print("unsuccessful login")
		

		#for e in users.objects.all():       #in case i need other way of logging in :  
			#if e.username == user_name and e.password == pass_word:
					#print("username and password do match")
			#else:
				#print("unsuccessful match")

				
			

  		  
		#return HttpResponseRedirect("") #i didnt knew it was this easy,














