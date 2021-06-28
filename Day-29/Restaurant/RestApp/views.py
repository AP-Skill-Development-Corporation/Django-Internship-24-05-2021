from django.shortcuts import render
from django.http import HttpResponse
from RestApp.forms import ReForm

# Create your views here.
def home(request):
	return render(request,'app/home.html')

def about(request):
	return render(request,'app/about.html')

def contact(request):
	return render(request,'app/contact.html')

def restlist(request):
	t = ReForm()
	return render(request,'app/restaurantlist.html',{'q':t})