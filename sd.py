import telebot

API_TOKEN = 'your_telegram_bot_api_token'
bot = telebot.TeleBot(6946944438:AAFlYUrAkmxFzZwUPHVXNXnmhN2txfVZ6dQ)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Charged Credit Card Checker Bot. Send me a credit card number to check its validity.")

@bot.message_handler(func=lambda message: True)
def check_credit_card(message):
    credit_card_number = message.text
    # Add your credit card validation logic here
    if is_valid_credit_card(credit_card_number):
        bot.reply_to(message, "The credit card is valid and charged.")
    else:
        bot.reply_to(message, "The credit card is invalid or not charged.")

def is_valid_credit_card(credit_card_number):
    # Implement credit card validation algorithm here
    return True  # Placeholder for validation logic

bot.polling()