from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length = 200, required=True)
    subject = forms.CharField(max_length = 300, required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=2000, required=True)