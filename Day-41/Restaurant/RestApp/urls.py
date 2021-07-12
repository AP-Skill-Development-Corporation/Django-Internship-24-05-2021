from django.urls import path
from RestApp import views
from django.contrib.auth import views as v

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cntct/',views.contact,name="ct"),
	path('rlist/',views.restlist,name="rstl"),
	path('rst/<int:m>/',views.rstup,name="rsup"),
	path('rsdlt/<int:n>/',views.rstdl,name="rsd"),
	path('rstviw/<int:a>/',views.rstvw,name="rsvw"),
	path('ilist/',views.itlist,name="itl"),
	path('ilstup/<int:d>/',views.itmup,name="itup"),
	path('ilstdl/<int:te>/',views.itmdl,name="itdl"),
	path('ilstvw/<int:p>/',views.itmvw,name="itmv"),
	path('rg/',views.usrreg,name="reg"),
	path('login/',v.LoginView.as_view(template_name="app/login.html"),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name="app/logout.html"),name="lgo"),
	path('roltype/',views.rolereq,name="rlrq"),
	path('gvper/',views.gveperm,name="gvpm"),
	path('gvup/<int:t>/',views.gvupd,name="gvup"),
	path('gvpr/<int:m>/',views.gvdlte,name="gvdl"),
	path('pfle/',views.pfle,name="pf"),
	path('pfupd/',views.pfleupd,name="pfup"),
	path('fdb/',views.feedback,name="fd"),
	path('chge/',views.changepwd,name="chpd"),
	path('itmd/<int:s>/',views.itemvew,name="itmvu"),
]