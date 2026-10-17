"""
This script uses yt-dlp to download audio, by year, from the
The Low Down podcast playlist.
"""

import yt_dlp

def download_playlist(playlist_url):
    """
    Downloads all audio from the podcast site.
    """
    ydl_opts = {
        "format": "bestaudio",
        "noplaylist": False,
        "ignoreerrors": True,
        "download_archive": "downloaded.log",
        "outtmpl": "%(upload_date>%Y)s/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",
            }
        ],
        'concurrent-fragments': True,
        'no-mtime': True,
        'playlistend': 10
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


if __name__ == "__main__":
    playlist = "https://rss2.flightcast.com/l2k5wawp71vbqbsc92xl6222.xml"
    download_playlist(playlist)
    print("Downloaded all audio from the The Low Down podcast website.")
