from utils.utils import get_crypto_price, get_dollar_rate, get_profit, get_loss, USD, ILS
from dotenv import load_dotenv
import os

# get env variables
load_dotenv()
token = os.getenv('TOKEN')
flat_buy_eth = float(os.getenv('FLAT_BUY_ETH'))
first_deposit = float(os.getenv('FIRST_DEPOSIT'))
chat_id = int(os.getenv('CHAT_ID'))
WEBHOOK_URL = os.getenv('WEBHOOK_URL')  # URL שבו הבוט שלך זמין, למשל https://your-app.onrender.com/

ETH = "ethereum"
# calculate basic data
ethereum_price = get_crypto_price(ETH)
my_balance_usd = flat_buy_eth * ethereum_price[USD]
my_balance_ils = my_balance_usd * get_dollar_rate()
