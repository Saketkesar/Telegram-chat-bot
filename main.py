#pip install python-telegram-bot
import telegram

from telegram.ext import *

import keys

print('Bot Started...')


# Lets us use the /start command
def start_command(update, context):
    update.message.reply_text('Hey There')


# Lets us use the /help command
def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')


# Lets us use the /custom command
def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_response(text) -> str:
    # Create your own response logic

    if 'hello' in text:
        return 'Hi there, friend!'

    if 'how are you' in text:
        return 'I\'m good and you?'

    if 'tell me some stuff about you' in text:
        return 'Well, I\'m not Saket, I\'m his virtual agent' 
        
    if 'who are you' in text:
        return 'Well, I\'m not Saket, I\'m his virtual agent'

    if 'what are you' in text:
        return 'Well, I\'m not Saket, I\'m his virtual agent'

    if 'Good' in text:
        return 'That\'s great'

    if 'Very good' in text:
        return 'That\'s great'  
    
    if 'Saket' in text:
        return 'Saket is passionate devloper and my creator'

    if 'bye' in text:
        return 'Great talk, see ya!'
    if 'fuck' in text:
        return 'Fuck yourself—Lord knows no one else will do it for you.'
    if 'fuck you' in text:
        return 'Fuck yourself—Lord knows no one else will do it for you.'

    if 'hi' in text:
        return 'hello'
    if 'fine' in text:
        return 'That\'s great'


     

    return 'I must be missing some knowledge. I\'ll have my developer look into this.'


def handle_message(update, context):
    # Get basic info of the incoming message
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    # Print a log for debugging
    

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if '@Saketkesarbot' in text:
            new_text = text.replace('@Saketkesarbot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    # Reply normal if the message is in private
    update.message.reply_text(response)


# Log errors
def error(update, context):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
