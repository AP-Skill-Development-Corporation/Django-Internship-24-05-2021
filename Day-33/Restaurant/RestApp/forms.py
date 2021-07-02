# from django.forms import ModelForm
from RestApp.models import Restaurant,Itemlist
from django import forms

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