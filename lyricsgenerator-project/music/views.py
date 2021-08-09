from django.shortcuts import render
from .forms import MusicForm


# Create your views here.
def home(request):
    return render(request, 'music/home.html')

def submit(request):
    if request.method == 'POST':
        # the image we have here!
        filled_form = MusicForm(request.POST)
        if filled_form.is_valid():
            note = "Thanks for submitting a new song! The song %s by %s is submitted!" %(filled_form.cleaned_data['songName'], 
            filled_form.cleaned_data['artist'],)
            filled_form = MusicForm()
        else :
            note = 'Music Submission has failed! try again.'
        return render(request, 'music/submit.html', {'musicform' : filled_form, 'note':note})
    else :
        form = MusicForm()
        return render(request, 'music/submit.html', {'musicform' : form})

def generate(request):
    # func
    return render(request, 'music/generate.html')

