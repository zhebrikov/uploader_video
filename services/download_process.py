import os

from download import download
from s3client import S3Client


async def download_process(link, update):
    await update.message.reply_text(f'Начинаем скачивать файл {link}')
    result = await download(link)
    await update.message.reply_text(f'Начинаем загрузку на облако {result['name']}')
    client = S3Client(
        endpoint_url=os.environ.get('STORAGE_ENDPOINT_URL'),
        access_key=os.environ.get('STORAGE_ACCESS_KEY'),
        secret_key=os.environ.get('STORAGE_SECRET_KEY'),
        bucket_name=os.environ.get('STORAGE_BUCKET_NAME'),
    )

    await client.upload_file('./{path}'.format(path=result['name']))

    os.remove('./{path}'.format(path=result['name']))

    await update.message.reply_text(f'Скачивание файла {link} Успешно закончено')