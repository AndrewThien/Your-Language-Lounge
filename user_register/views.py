from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def user_register(request):
    
	""" There are two checking in this function:
 1- The first checks if the form is being posted
 2- The second checks if the form is valid
	
	If both check's results are True, then the form information will be saved under a user, 
 he/she will be logged in and re-direct to register_sucess page eventually.
	
 	"""
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			   
			return redirect('user_register:register_success')

		messages.error(request, "Sorry, registration was unsuccessful because of invalid information.")
  
	form = NewUserForm()
	return render (request=request, template_name="user_register/register.html", context={"register_form":form}) 

def register_success(request):
    return render(request, 'user_register/register_success.html')