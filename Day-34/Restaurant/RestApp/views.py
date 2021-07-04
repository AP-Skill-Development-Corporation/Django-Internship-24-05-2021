from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm,ItemsForm,UsgForm
from RestApp.models import Restaurant,Itemlist
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

# Create your views here.
def home(request):
	w = Restaurant.objects.all()
	return render(request,'app/home.html',{'c':w})

def about(request):
	return render(request,'app/about.html')

def contact(request):
	return render(request,'app/contact.html')

@login_required
def restlist(request):
	y = Restaurant.objects.all()
	if request.method == "POST":
		t = ReForm(request.POST,request.FILES)
		if t.is_valid():
			t.save()
			messages.success(request,"Restaurant Added Successfully")
			return redirect('/rlist')
	t = ReForm()
	return render(request,'app/restaurantlist.html',{'q':t,'a':y})

@login_required
def rstup(request,m):
	k = Restaurant.objects.get(id=m)
	if request.method == "POST":
		e = ReForm(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			# print(k.rname)
			messages.warning(request,"{} Restaurant Updated Successfully".format(k.rname))
			return redirect('/rlist')
	e = ReForm(instance=k)
	return render(request,'app/restupdate.html',{'x':e})

@login_required
def rstdl(request,n):
	v = Restaurant.objects.get(id=n)
	if request.method == "POST":
		messages.info(request,"{} Restaurant Deleted Successfully".format(v.rname))
		v.delete()
		return redirect('/rlist')
	return render(request,'app/restdelete.html',{'q':v})

@login_required
def rstvw(request,a):
	s = Restaurant.objects.get(id=a)
	return render(request,'app/restview.html',{'z':s})

@login_required
def itlist(request):
	m = Itemlist.objects.all()
	if request.method == "POST":
		k = ItemsForm(request.POST,request.FILES)
		if k.is_valid():
			n = k.save(commit=False)
			messages.success(request,'{} Item is Added Successfully'.format(n.iname))
			n.save()
			return redirect('/ilist')
	k = ItemsForm()
	return render(request,'app/itmlist.html',{'r':k,'s':m})


def usrreg(request):
	if request.method == "POST":
		d = UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/login')
	d = UsgForm()
	return render(request,'app/usrregister.html',{'t':d})