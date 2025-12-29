from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment

API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_youtube(song_name):
    youtube = build(
        "youtube",
        "v3",
        developerKey=API_KEY
    )

    request = youtube.search().list(
        q=song_name,
        part="snippet",
        type="video",
        maxResults=1
    )

    response = request.execute()

    if response["items"]:
        video_id = response["items"][0]["id"]["videoId"]
        return f"https://www.youtube.com/watch?v={video_id}"

    return None
