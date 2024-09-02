# Using putube a popular python library to download audios and visdeos from youtube
# Read the docs: https://pytube.io
# Mutagen library aims to be an all purpose multimedia tagging library which in our case can add metadata to a multimedia

from pytube import YouTube
import requests
from mutagen.mp4 import MP4, MP4Cover


def download_from_youtube(url):
    """A function that takes the URL of the YouTube video and downloads the audio from that URL"""
    try:
        yt = YouTube(url)
        # getting the title, thumbnail  of the video
        artist = yt.author
        title = yt.title
        thumbnail = yt.thumbnail_url
        print(title, thumbnail)
        # SELECT THE STREAM YOU WANT TO DOWNLOAD
        # .streams returns a list of media streams that is available for a particular video
        # you can chose between adaptive vs progressive streaming method
        # Read the docs
        stream = yt.streams.filter(
            adaptive=True, only_audio=True, file_extension='mp4')
        print(stream)
        # selecting the correct object from the list of stream
        selected_stream = stream[-1]
        print(selected_stream)

        # !!!!  Download(returns file path) and save file path(THIS DOWNLADS !!)
        audio_file_path = selected_stream.download()

        print(f"The downloaded file path is: {audio_file_path}")
        print("Your song has been downloaded!")

        # Download the thumbnail art
        response = requests.get(thumbnail)
        thumbnail_data = response.content

        # Add the thumbnail as cover art and set artist and album name
        audio = MP4(audio_file_path)
        audio['covr'] = [
            MP4Cover(thumbnail_data, imageformat=MP4Cover.FORMAT_JPEG)]
        audio['\xa9ART'] = artist  # Set artist name
        audio.save()

        print(
            f"Downloaded and added cover art, artist, and album name to {audio_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Url of 
URL = "https://youtu.be/J4DmU_On6ag"


if __name__ == "__main__":
    download_from_youtube(URL)
