from http.client import IncompleteRead
from django.shortcuts import render,redirect
from django.contrib import messages
from clip.forms import YoutubeVideoForm
from clip.utils import youtube_video

# Create your views here.


def youtube(request):
    if request.method == 'POST':
        form = YoutubeVideoForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['video_url']
            quality = form.cleaned_data['quality']
            try:
                youtube_video(video_url, quality)
                messages.success(request, 'Video downloaded successfully!')
            except IncompleteRead:
                messages.error(
                    request, 'An error occurred: The download was incomplete. Due to Network Error. Please try again later.')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
            return redirect('index')
    else:
        youtube_form = YoutubeVideoForm()
    return render(request, 'index.html', {'youtube_form': youtube_form})
