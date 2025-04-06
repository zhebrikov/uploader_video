import os

from telegram.ext import ApplicationBuilder, CommandHandler

from chat import upload

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.environ.get('TELEGRAM_BOT_KEY')).build()

    app.add_handler(CommandHandler("upload", upload))

    app.run_polling()
    #asyncio.run()