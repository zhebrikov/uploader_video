from telegram import Update
from telegram.ext import ContextTypes
import logging

from services.download_process import download_process

logger = logging.getLogger(__name__)

async def upload(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        link = update.message.text.replace("/upload", "").strip()
        await download_process(link, update)
    except BaseException as e:
        logger.error(e)
        await update.message.reply_text(f'При скачивании файла {link} Произошла ошибка')
