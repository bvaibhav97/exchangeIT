from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import View 
from .forms import free_form
from .models import freelance_basic
from django.http import HttpResponseRedirect




class freelance_home(TemplateView):
	template_name = "freelance_home.html"

	def get(self, request):
		# <view logic>
		Qset = freelance_basic.objects.all()
		context = { 
		'queryset': Qset
		
		}
		#'session_key', 'set_expiry'#
		print(request.session.session_key)
		request.session.set_expiry(500)
		request.session["fav_color"] = "orange"
		template_name = "freelance_home.html"
		print(request.session.session_key)
		print(type(request.session))
		return render(request,'freelance_home.html', context)
	




class basic_form(View):
	template_name="basic_form.html"
	model = freelance_basic 

	template_name= "signup.html" 

	def get(self, request, *args, **kwargs ):
		forminstance = free_form()	
		context = { 
		'form': forminstance
		
		}
		return render(request,'signup.html', context)
		...  # code to process a GET request

	def post(self, request, *args, **kwargs ):
		Title = request.POST.get("Title")
		Description = request.POST.get("Description")
		print(Title)
		freedb = freelance_basic() #its a great discovery , making an object of the db modeel
		freedb.Title= Title 
		freedb.Description= Description 

		#n literally storing new daya in object
		freedb.save() #n saving it permanantly
		return HttpResponseRedirect("") #i didnt knew it was this easy,
