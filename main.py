import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from predictor import Predictor
from utils import start_timer, stop_timer

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_CHAT_ID"))

predictor = Predictor()
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

def restricted(func):
    def wrapper(update, context):
        if update.effective_chat.id != ADMIN_ID:
            return
        return func(update, context)
    return wrapper

@restricted
def start_bot(update, context):
    start_timer(predictor, context.bot)
    update.message.reply_text("✅ Bot started!")

@restricted
def stop_bot(update, context):
    stop_timer(predictor)
    update.message.reply_text("⛔ Bot stopped!")

@restricted
def status(update, context):
    update.message.reply_text(predictor.get_status())

dp.add_handler(CommandHandler("start", start_bot))
dp.add_handler(CommandHandler("stop", stop_bot))
dp.add_handler(CommandHandler("status", status))

updater.start_polling()
