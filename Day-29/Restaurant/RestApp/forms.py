from django.forms import ModelForm
from RestApp.models import Restaurant


class ReForm(ModelForm):
	class Meta:
		model = Restaurant
		fields = "__all__"
