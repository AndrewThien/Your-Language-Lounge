from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def user_register(request):
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