from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'music/home.html')

def submit(request):
    return render(request, 'music/submit.html')