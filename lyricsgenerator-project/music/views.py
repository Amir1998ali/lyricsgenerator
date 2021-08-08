from django.shortcuts import render
from .forms import MusicForm

# Create your views here.
def home(request):
    return render(request, 'music/home.html')

def submit(request):
    if request.method == 'POST':
        filled_form = MusicForm(request.POST)
        if filled_form.is_valid():
            note = "Thanks for submitting a new song! The song %s by %s is submitted!" %(filled_form.cleaned_data['songName'], 
            filled_form.cleaned_data['artist'],)

            new_form = MusicForm()
            return render(request, 'music/submit.html', {'musicform' : new_form, 'note':note})
    else :
        form = MusicForm()
        return render(request, 'music/submit.html', {'musicform' : form})

def generate(request):
    return render(request, 'music/generate.html')