from django import forms
from .models import Subscription
from django.forms import ModelChoiceField

class SubscriptionForm(forms.ModelForm):
	
	class Meta:
		model = Subscription
		fields = ['sub_paper','start_date','address']