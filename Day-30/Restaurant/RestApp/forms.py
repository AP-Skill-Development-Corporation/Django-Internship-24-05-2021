# from django.forms import ModelForm
from RestApp.models import Restaurant
from django import forms

class ReForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ["rname","nitems","timings","address"]
		widgets = {
		"rname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Restaurant Name",
			}),
		"nitems":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Number of Items available in Restaurant",
			}),
		"timings":forms.TimeInput(attrs={
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
