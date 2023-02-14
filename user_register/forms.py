from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    
	""" This new class calls the 'UserCreationForm', which is a pre-built register form from Django connected to the pre-built model 'User'.
 This form then is customised by adding 'email' and 'first_name' fields to it. 

    """
        
	first_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "password1", "password2", "first_name","email")

	def save(self, commit=True):
     
		""" Save method  """
  
		user = super(NewUserForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user