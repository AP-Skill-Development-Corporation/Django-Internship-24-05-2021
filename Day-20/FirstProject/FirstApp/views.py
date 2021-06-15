from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse("Hi Good Evening to All...")

def htmltag(req):
	return HttpResponse("<h2>Hi Welcome to APSSDC Programs</h2>")

def usernameprint(request,uname):
	return HttpResponse("<h2>Hi Welcome <span style='color:green'>{}</span></h2>".format(uname))

def usernameage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center;background-color:green;padding:23px'>Hi User <span style='color:yellow'>{}</span> and your age is: <span style='color:red'>{}</span></h3>".format(un,ag))


def empdetails(request,eid,ename,eage):
	return HttpResponse("<script>alert('Hi Welcome {}')</script><h3>Hi Welcome {} and your age is: {} and your id is: {}</h3>".format(ename,ename,eage,eid))

def htm(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def empname(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/std.html')

def internalJS(request):
	return render(request,'html/internalJS.html')

def myform(req):
	if req.method=="POST":
		#print(req.POST)
		uname = req.POST['uname']
		rollno = req.POST['rollno']
		email = req.POST.get('email')
		#print(uname,rollno,email)
		data = {'username':uname,'rno':rollno,'emailId':email}
		return render(req,'html/display.html',data)


	return render(req,'html/myform.html')






