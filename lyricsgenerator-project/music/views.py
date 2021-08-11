from django.shortcuts import render
from .forms import MusicForm
import lyricsgenius as lg

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
            

            _file = open("/Users/mohseniamirali/Desktop/generator/lyricsgenerator-project/lyricsgenerator/texts.txt", "w")


            artist = filled_form.cleaned_data['artist']
            songname = filled_form.cleaned_data['songName']
            genius = lg.Genius('K1TXu3BGIWFtX6Cxf7ch2XZW95m40-9HMWIo9f0gZaQz16RF-6BXstfVDnOSbTp0', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

            def get_lyrics(arr, song, k):  # Write lyrics of k songs by each artist in arr
                c = 0  # Counter
                for name in arr:
                    try:
                        # songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
                        # s = [song.lyrics for song in songs]
                        song = genius.search_song(song, arr[0])
                        s = song.lyrics 
                        _file.write(s)  # Deliminator
                        c += 1
                        print(f"Songs grabbed:{len(s)}")
                    except:  #  Broad catch which will give us the name of artist and song that threw the exception
                        print(f"some exception at {name}: {c}")

            get_lyrics([artist], songname, 1)
            _file.close()
            _file = open('/Users/mohseniamirali/Desktop/generator/lyricsgenerator-project/lyricsgenerator/texts.txt', 'r')
            tmp = _file.readlines()
            generated = ""
            # for i in tmp:

            filled_form = MusicForm()
            print(generated)
            _file.close()
            return render(request, 'music/generate.html', {'tmp' : tmp})
            
        else :
            
            note = 'Music Submission has failed! try again.'
            return render(request, 'music/submit.html', {'musicform' : filled_form, 'note':note})
    else :
        form = MusicForm()
        return render(request, 'music/submit.html', {'musicform' : form})

def generate(request):
    # func

    
    genius = lg.Genius('K1TXu3BGIWFtX6Cxf7ch2XZW95m40-9HMWIo9f0gZaQz16RF-6BXstfVDnOSbTp0', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

    artist = "Eminem"
    def get_lyrics(arr, k):  # Write lyrics of k songs by each artist in arr
        c = 0  # Counter
        for name in arr:
            try:
                songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
                s = [song.lyrics for song in songs]
                file.write("\n \n   <|endoftext|>   \n \n".join(s))  # Deliminator
                c += 1
                print(f"Songs grabbed:{len(s)}")
            except:  #  Broad catch which will give us the name of artist and song that threw the exception
                print(f"some exception at {name}: {c}")


    get_lyrics([artist], 1)

    with open('/Users/mohseniamirali/Desktop/generator/lyricsgenerator-project/lyricsgenerator/texts.txt') as f:
        lines = f.readlines()
        print(lines)
    
    
    return render(request, 'music/generate.html')