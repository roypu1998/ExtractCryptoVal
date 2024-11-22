from utils.declear import chat_id, my_balance_ils, get_profit, first_deposit
from bot.bot import bot
from time import sleep
import threading


def run_bot():
    print("bot start")
    bot.infinity_polling()

def run_main():
    print('main start')
    while True:
        if (my_balance_ils - first_deposit) > 500:
            bot.send_message(chat_id=chat_id, text=f'{get_profit(my_balance_ils, first_deposit)}')
        sleep(5)

if __name__ == '__main__':
    thread_bot = threading.Thread(target=run_bot)
    sleep(5)
    thread_main = threading.Thread(target=run_main)
    thread_bot.start()
    thread_main.start()
