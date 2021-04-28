import youtube_dl
import json
from time import sleep as s
from logger import downloader_logger
def log():
    downloader_logger.info('test')
def get_links():
    links = []
    for _ in range(int(input('How many links are you going to download?: '))):
        link = input('Input the links to be downloaded: ')
        links.append(link)
    return links

def log():
    downloader_logger.info('test')

def download(links):
    options = {
        'noplaylist': True,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        downloader_logger.info('test')
        for link in links:
            info_dict = ydl.extract_info(link)
            video_url = info_dict.get('url', None)
            video_id = info_dict.get('id', None)
            video_title = info_dict.get('title', None)

            # ydl.download(links)