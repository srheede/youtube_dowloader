import yt_dlp
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def downloader(url):
    # Get username and password from environment variables
    username = os.getenv('YOUTUBE_USERNAME')
    password = os.getenv('YOUTUBE_PASSWORD')

    ydl_opts = {
        'username': username,
        'password': password,
        'format': 'best',
        'progress_hooks': [lambda d: print(f"Status: {d['status']}") if d['status'] == 'finished' else None]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for the YouTube URL
url = input("Please enter the YouTube video URL: ")
downloader(url)
