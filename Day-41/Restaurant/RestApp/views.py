from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm,ItemsForm,UsgForm,Rltype,Rlupd,Pfupd,Chgepwd
from RestApp.models import Restaurant,Itemlist,Rolereq,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail
from Restaurant import settings

# Create your views here.
def home(request):
	w = Restaurant.objects.filter(uid_id=request.user.id)
	t = Restaurant.objects.all()
	return render(request,'app/home.html',{'c':w,'y':t})

def about(request):
	return render(request,'app/about.html')

def contact(request):
	return render(request,'app/contact.html')

@login_required
def restlist(request):
	y = Restaurant.objects.filter(uid_id=request.user.id)
	if request.method == "POST":
		t = ReForm(request.POST,request.FILES)
		if t.is_valid():
			c = t.save(commit=False)
			c.uid_id = request.user.id
			c.save()
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
	st = list(Restaurant.objects.filter(uid_id=request.user.id))
	mm = Itemlist.objects.all()
	d,i = {},0
	for mp in mm:
		for h in st:
			if mp.rsid_id == h.id:
				d[i] = mp.iname,mp.icategory,mp.price,mp.iimage,mp.itavailability,mp.id,h.rname
				i = i+1
	if request.method == "POST":
		k = ItemsForm(request.POST,request.FILES)
		if k.is_valid():
			n = k.save(commit=False)
			messages.success(request,'{} Item is Added Successfully'.format(n.iname))
			n.save()
			return redirect('/ilist')
	k = ItemsForm()
	return render(request,'app/itmlist.html',{'r':k,'er':st,'s':d.values()})

@login_required
def itmup(request,d):
	t = Itemlist.objects.get(id=d)
	if request.method == "POST":
		z = ItemsForm(request.POST,request.FILES,instance=t)
		if z.is_valid():
			z.save()
			messages.info(request,"{} Item Updated Successfully".format(t.iname))
			return redirect('/ilist')
	z = ItemsForm(instance=t)
	return render(request,'app/itemupdate.html',{'s':z})

@login_required
def itmdl(request,te):
	p = Itemlist.objects.get(id=te)
	if request.method == "POST":
		messages.waring(request,"{} Restaurant Deleted Successfully".format(p.iname))
		p.delete()
		return redirect('/ilist')
	return render(request,'app/itemdl.html',{'a':p})

@login_required
def itmvw(request,p):
	n = Itemlist.objects.get(id=p)
	return render(request,'app/itmvw.html',{'d':n})

def usrreg(request):
	if request.method == "POST":
		d = UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/login')
	d = UsgForm()
	return render(request,'app/usrregister.html',{'t':d})

@login_required
def rolereq(request):
	p = Rolereq.objects.filter(ud_id=request.user.id).count()
	if request.method == "POST":
		k = Rltype(request.POST,request.FILES)
		if k.is_valid():
			y = k.save(commit=False)
			y.ud_id = request.user.id
			y.uname = request.user.username
			y.save()
			return redirect('/')
	k = Rltype()
	return render(request,'app/rolereq.html',{'d':k,'c':p})

@login_required
def gveperm(request):
	u = User.objects.all()
	r = Rolereq.objects.all()
	d = {}
	for n in u:
		for m in r:
			if n.is_superuser == 1 or n.id != m.ud_id:
				continue
			else:
				d[m.id] = m.uname,m.rltype,n.role,n.id,m.id
	return render(request,'app/gvper.html',{'h':d.values()})

@login_required
def gvupd(request,t):
	y = Rolereq.objects.get(ud_id=t)
	d = User.objects.get(id=t)
	if request.method == "POST":
		n = Rlupd(request.POST,instance=d)
		if n.is_valid():
			n.save()
			y.is_checked = 1
			y.save()
			return redirect('/gvper')
	n = Rlupd(instance=d)
	return render(request,'app/gvepermsion.html',{'c':n})

@login_required
def gvdlte(request,m):
	n = Rolereq.objects.get(id=m)
	t = User.objects.get(id=n.ud_id)
	if request.method == "POST":
		n.delete()
		t.role = 1
		t.save()
		return redirect('/gvper')
	return render(request,'app/gvdlte.html',{'d':n})

@login_required
def pfle(request):
	return render(request,'app/profile.html')

@login_required
def feedback(request):
	if request.method == "POST":
		sd = request.POST['snmail'].split(',')
		sm = request.POST['sub']
		mg = request.POST['msg']
		rt = settings.EMAIL_HOST_USER
		dt = send_mail(sm,mg,rt,sd)
		if dt == 1:
			return redirect('/')
	return render(request,'app/feedback.html')

@login_required
def pfleupd(request):
	t = User.objects.get(id=request.user.id)
	if request.method == "POST":
		pfl = Pfupd(request.POST,request.FILES,instance=t)
		if pfl.is_valid():
			pfl.save()
			return redirect('/pfle')
	pfl = Pfupd(instance=t)
	return render(request,'app/pfleupdate.html',{'u':pfl})

@login_required
def changepwd(request):
	if request.method == "POST":
		k = Chgepwd(user=request.user,data=request.POST)
		if k.is_valid():
			k.save()
			return redirect('/login')
	k = Chgepwd(user=request)
	return render(request,'app/changepwd.html',{'t':k})

@login_required
def itemvew(request,s):
	r = Itemlist.objects.filter(rsid_id=s)
	return render(request,'app/itemuser.html',{'tq':r})
