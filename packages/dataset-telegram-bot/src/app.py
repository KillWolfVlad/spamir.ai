from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler

from .config import config
from .handlers import message, start

app = ApplicationBuilder().token(config.telegram_bot_token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(None, message))
