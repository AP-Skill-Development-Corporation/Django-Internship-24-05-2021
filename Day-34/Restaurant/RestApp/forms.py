# from django.forms import ModelForm
from RestApp.models import Restaurant,Itemlist
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
		fields = ['iname','icategory','price','itavailability','iimage']
		widgets = {
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