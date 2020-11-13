from django import forms
from .models import planetas

class planetasForm(forms.ModelForm):
	class Meta:
		model = planetas
		fields = ['planeta', 'tipo', 'massa']

