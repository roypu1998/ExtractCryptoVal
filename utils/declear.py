from utils.utils import get_crypto_price, get_dollar_rate, get_profit, get_loss
from dotenv import load_dotenv
import os

# get env variables
load_dotenv()
token = os.getenv('TOKEN')
flat_buy_eth = float(os.getenv('FLAT_BUY_ETH'))
first_deposit = float(os.getenv('FIRST_DEPOSIT'))
chat_id = int(os.getenv('CHAT_ID'))

# calculate basic data
ethereum_price = get_crypto_price("ethereum")
my_balance_usd = flat_buy_eth * ethereum_price["usd"]
my_balance_ils = my_balance_usd * get_dollar_rate("ILS")
