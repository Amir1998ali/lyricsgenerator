from django import forms
from .models import Music

# class MusicForm(forms.Form):
#     # represent the music form we wanna create
#     artist = forms.CharField(label = "Artist", max_length=100)
#     songName = forms.CharField(label = "Song Name", max_length=100)
#     lyrics = forms.CharField(label = "Lyrics", max_length=10000)

# you can submit different files
class MusicForm(forms.ModelForm):

    class Meta:
        model = Music
        fields = ['artist', 'songName']
        labels = {'artist' : 'Artist' , 'songName' : 'Song Name'}
