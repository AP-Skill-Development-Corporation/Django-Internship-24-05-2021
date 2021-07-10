# from django.forms import ModelForm
from RestApp.models import Restaurant,Itemlist,User,Rolereq
from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm


class ReForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ["rname","nitems","timings","rsimg","address"]
		widgets = {
		"rname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Restaurant Name",
			}),
		"nitems":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Number of Items available in Restaurant",
			}),
		"timings":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter timings",
			"type":"time",
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Address",
			"rows":3,
			}),
		}

class ItemsForm(forms.ModelForm):
	class Meta:
		model = Itemlist
		fields = ['rsid','iname','icategory','price','itavailability','iimage']
		widgets = {
		"rsid":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Select Restaurant",
			# "readonly":True,
			}),
		"iname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Item Name",
			}),
		"icategory":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Select Item",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Price",
			}),
		'itavailability':forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class UsgForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Password",
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		}

class Rltype(forms.ModelForm):
	class Meta:
		model = Rolereq
		fields = ["uname","rltype","pfe"]
		widgets = {
		"rltype":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class Rlupd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","role"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"role":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class Pfupd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","age","mobilenumber","uimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Email",
			}),
		"age":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Age",
			}),
		"mobilenumber":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Mobile Number",
			}),
		}

class Chgepwd(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Old Password"
		}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Password",
		}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["old_password","new_password1","new_password2"]