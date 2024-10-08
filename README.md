# YouTube Audio Downloader

This repository contains a Python script that allows users to download audio from YouTube videos. The script uses the `pytube` library to handle the downloading process and the `mutagen` library to add metadata to the downloaded audio files.

## Features
- Download audio from YouTube videos.
- Add cover art, artist name, and album name to the downloaded audio files.

## Libraries Used
- **pytube**: A popular Python library for downloading videos and audio from YouTube. Read the docs: pytube.io
- **mutagen**: A multimedia tagging library that can add metadata to multimedia files.

## Fixes
The official `pytube` library has an issue that has been fixed in this code. The script ensures that the audio download and metadata addition work seamlessly.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/youtubeDownloader_Python.git
   cd youtubeDownloader_Python
2. Install the required libraries
    pip install pytube
    pip install mutagen
    pip install requests

## Usage
    Open the download_from_youtube.py file.
    Replace the URL variable with the URL of the YouTube video you want to download.
    Run the script:
    python download_from_youtube.py


## Edit:
1. If you are having issues with your pytube package please change the following lines of code:
    From: venv/Lib/site-packages/pytube/cipher.py
2. Line number: 411 to: 
    transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)


