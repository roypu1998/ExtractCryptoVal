from utils.declear import *
from bot.bot import run, bot
from time import sleep
import threading

if __name__ == '__main__':
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        if my_balance_ils > first_deposit:
            bot.send_message(chat_id=chat_id, text=f'{get_profit(my_balance_ils, first_deposit)}')
        sleep(5)
