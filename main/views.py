from django.shortcuts import render
from .forms import SongForm
from pytube import YouTube
import os
import pytube

# Create your views here.

def home(request):
    if request.method =='POST':
        #form = SongForm(request.POST)
        #print("xxx" + form.url)

        #if form.is_valid():

        url = request.POST.get('url')
        #loaction = request.POST.get('location')
        if(url):
            print(url)
            yt = YouTube(url)
            print(yt)
            video = yt.streams.get_audio_only()
            destination = "C:/Users/user/Downloads"

            out_file = video.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(yt.title + " has been successfully downloaded.")


    return render(request,'home.html',{})