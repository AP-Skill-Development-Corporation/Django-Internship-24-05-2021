from django.urls import path
from RestApp import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cntct/',views.contact,name="ct"),
]