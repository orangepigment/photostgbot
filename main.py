import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
SUPPORT_GROUP_ID = os.getenv('SUPPORT_GROUP_ID')

# Log to file or something
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет! Пришли мне фото, которое ты хочешь увидеть дополненным в канале Слой за слоем."
    )


async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Resend photo to support group
    await context.bot.send_photo(
        chat_id=SUPPORT_GROUP_ID,
        # ToDo: support multiple photos
        photo=update.message.photo[0].file_id,
        caption='Новое предложенное фото'
    )
    # Thank the user
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Спасибо за фото)"
    )


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Пожалуйста, приложи фото к сообщению)"
    )


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    photo_handler = MessageHandler(filters.PHOTO & (~filters.COMMAND), photo)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(start_handler)
    application.add_handler(photo_handler)
    application.add_handler(unknown_handler)

    application.run_polling()
