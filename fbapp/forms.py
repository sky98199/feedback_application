from django import forms
from .models import FbModel

class FbForm(forms.ModelForm):
	class Meta:
		model=FbModel
		fields=['name','feedback']

		widgets={'feedback':forms.Textarea(attrs={'style':'resize:none','rows':5}),
				'name':forms.TextInput(attrs={'style':'width:700'})}