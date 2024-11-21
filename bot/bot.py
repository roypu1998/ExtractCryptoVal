from telebot import TeleBot
from utils.declear import *

bot = TeleBot(token=token)

@bot.message_handler(commands=['start'])
def send_about(msg):
    bot.send_message(chat_id=msg.chat.id, text="Bot Start")

@bot.message_handler(commands=['calc'])
def send_about(msg):
    msg_bck = (f'The price of Ethereum in USD is {ethereum_price['usd']}$'
               f'\nThe price of Ethereum in ILS is {ethereum_price['ils']}₪'
               f'\nYour crypto flat buy is: {flat_buy_eth} ETH and {my_balance_usd}$ and {my_balance_ils}₪')
    bot.send_message(chat_id=msg.chat.id, text=f'{msg_bck}')
    if my_balance_ils > first_deposit:
        bot.send_message(chat_id=msg.chat.id, text=f'{get_profit(my_balance_ils, first_deposit)}')
    else:
        bot.send_message(chat_id=msg.chat.id, text=f'{get_loss(my_balance_ils, first_deposit)}')

@bot.message_handler(commands=['is_alive'])
def send_about(msg):
    bot.send_message(chat_id=msg.chat.id, text="Bot Alive")


def run():
    print("bot start")
    bot.infinity_polling()


