from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
# parts abpput contact us form was taken and adapted from https://learndjango.com/tutorials/django-email-contact-form-tutorial and https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend
def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            body = {
            'name': form.cleaned_data["name"],
            'email': form.cleaned_data["email"],
            'subject': form.cleaned_data["subject"],
            'message' : form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, email, ['anretrithien@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("contact_us:success")
    return render(request, "contact_us/contact_us.html", {"form": form})

def successView(request):
    return render(request, 'contact_us/success.html')