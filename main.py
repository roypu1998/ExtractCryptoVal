from utils.declear import chat_id, my_balance_ils, get_profit, first_deposit
from bot.bot import thread, bot
from time import sleep


if __name__ == '__main__':
    while True:
        if my_balance_ils > first_deposit:
            bot.send_message(chat_id=chat_id, text=f'{get_profit(my_balance_ils, first_deposit)}')
        sleep(5)
