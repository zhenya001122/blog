from asgiref.sync import sync_to_async
from django.conf import settings
from django.core.cache import cache
from telegram import Update, Bot
from telegram.ext import ContextTypes

from hectar.models import Message
from shop.models import Product


@sync_to_async
def create_message(action: str, text: str):
    Message.objects.create(action=action, text=text, message={})


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cache.set("chat_id", update.effective_chat.id, 60 * 60 * 24)
    await update.message.reply_text(f"Start {update.effective_user.first_name}")


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await create_message(action="message", text=update.message.text)
    await update.message.reply_text(f"Message {update.effective_user.first_name}")


async def send_message(chat_id: int, text: str) -> None:
    bot = Bot(settings.BOT_TOKEN)
    chat_id = cache.get("chat_id")
    await bot.send_message(chat_id=chat_id, text=text)

