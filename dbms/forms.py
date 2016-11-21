from django.contrib.auth.models import User
from django import forms
from .models import UserProfile,Project
PROJECTS=(
('primenos','primenos'),
('localmin','localmin'),
)

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['username','email','password']

class Projectmgmt(forms.ModelForm):
	error_css_class='error'
	#projects=forms.ModelMultipleChoiceField(queryset=Project.objects.all(),widget=forms.SelectMultiple())
	projects=forms.MultipleChoiceField(choices=PROJECTS,widget=forms.SelectMultiple())
	class Meta:
		model=UserProfile
		
		exclude=['user']
