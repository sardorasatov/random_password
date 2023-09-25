import logging
from telegram.ext import Updater, CommandHandler, MessageHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Define command handlers
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your bot.")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Set up the bot
def main():
    # Create the Updater and pass in your bot token
    updater = Updater(token='6697177535:AAGr00Z0kyeWM9I6zaZaQY_wWip2c--D8WA', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Add message handler
    echo_handler = MessageHandler( echo)
    dispatcher.add_handler(echo_handler)

    # Start the bot
    updater.start_polling()
