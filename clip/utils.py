import os
from pytube import YouTube
from pytube.cli import on_progress



def youtube_video(video_url, quality='highest'):
    try:
        # Create a YouTube object with the provided video URL
        yt = YouTube(video_url, on_progress_callback=on_progress)

        # Get the stream based on the selected quality
        if quality == 'highest':
            stream = yt.streams.get_highest_resolution()
        elif quality == 'lowest':
            stream = yt.streams.get_lowest_resolution()
        else:
            stream = yt.streams.filter(res=quality).first()

        # Define the save path dynamically based on the operating system
        save_path = os.path.join(os.path.expanduser('~'), 'Downloads')

        # Download the video
        stream.download(output_path=save_path)

        print("\nVideo downloaded successfully!")
    except Exception as e:
        print("\nAn error occurred:", str(e))


