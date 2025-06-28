import requests


async def add_video(name, link):
    url = 'https://apivideo.zheev.ru/video/'
    body = {
        "name": name,
        "link": link
    }

    requests.post(url, json=body)