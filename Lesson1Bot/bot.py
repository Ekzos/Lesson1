from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext # Updater соединяется с Телеграмм и проверяет есть ли новые сообщения
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', 
                    level=logging.INFO,
                    filename='bot.log'
                    )

def starting_chat(update: Update, context: CallbackContext): # (bot, update) не работает, не понятно почему
    text = 'Начало чата'
    print(text)
    update.message.reply_text(text)

# ФУНКЦИЯ с минимальным телом бота: создаю бота, говорю ходить на платформу и работать бесконечно
def main():
    mybot = Updater("2024805449:AAEbBSD0sXm1cvOdStG95zA32sFCAAyp-6U")

    logging.INFO=('Бот запускается')
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', starting_chat)) # добавление обработчика команд
    
    mybot.start_polling() # mybot, начни регулярно ходить на платформу телеграмм и проверять наличие сообщений
    mybot.idle() # mybot будет работать до тех пор, пока я его принудительно не остановлю (CTRL + C)

# Вызов функции - запуск бота
main()

