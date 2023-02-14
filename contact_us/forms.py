from django import forms

class ContactForm(forms.Form):
    """ Create a ContactForm class with the pre-built form from Django.
    Then, declare the fields and their conditions    
    """
    name = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length = 200, required=True)
    subject = forms.CharField(max_length = 300, required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=2000, required=True)