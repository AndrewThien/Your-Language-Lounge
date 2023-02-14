from django.shortcuts import render

# Create your views here.
def our_values(request):
    return render(request, 'why_us/our_values.html')

def our_teachers(request):
    return render(request, 'why_us/our_teachers.html')