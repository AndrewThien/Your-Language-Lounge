from django.shortcuts import render

# Create your views here.
def communicative(request):
    return render(request, 'classes/Communicative.html')

def ielts(request):
    return render(request, 'classes/IELTS.html')