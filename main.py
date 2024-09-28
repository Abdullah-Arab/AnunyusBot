import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Load environment variables from the .env file
load_dotenv()

# Fetch the bot token and other sensitive data from the environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
OWNER_ID = os.getenv('OWNER_ID')  # This is optional, use if needed

# Start command
def start(update, context):
    update.message.reply_text("Welcome to the Anonymous Messaging Bot!")

# Handle incoming messages
def handle_message(update, context):
    user = update.message.from_user  # Get the user who sent the message
    message_text = update.message.text  # Get the text of the message

    # Log or print the sender's information (for the bot owner)
    print(f"Sender: {user.username} (ID: {user.id}) - Message: {message_text}")

    # Send a response to the sender
    update.message.reply_text("Your anonymous message has been received!")

    # Send the message and sender's info to the bot owner (you)
    if OWNER_ID:
        context.bot.send_message(
            chat_id=OWNER_ID,
            text=f"Anonymous message from {user.username} (ID: {user.id}): {message_text}"
        )

# Main function to run the bot
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler("start", start))

    # Message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
