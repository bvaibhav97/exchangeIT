from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class HomePage(TemplateView):
	template_name= "abc.html"



  
   