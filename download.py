import logging
import time

from pytubefix import YouTube
from pytubefix.cli import on_progress

async def download(url: str):
    logger = logging.getLogger(__name__)
    try:
        yt = YouTube(url,on_progress_callback = on_progress)
        title = yt.title
        ys = yt.streams.get_highest_resolution()
        name = '{name}.mp4'.format(name=time.time())
        ys.download(output_path='./', filename=name)

        return {'name': name, 'title': title}
    except BaseException as e:
        logger.error(e)
        raise e
