import requests

USD = 'usd'
ILS = 'ils'

def get_dollar_rate(to_currency='ILS'):
    # URL for the free exchange rate API
    url = "https://open.er-api.com/v6/latest/USD"
    # Send a GET request to the API
    response = requests.get(url)
    # Parse the JSON response
    data = response.json()
    # Extract the exchange rate for a specific currency, e.g., ILS
    return data['rates'][to_currency]

def get_crypto_price(crypto_id, currency='usd,ils'):
    url = f'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': crypto_id,
        'vs_currencies': currency
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data[crypto_id]

def get_profit(balance, deposit):
    return f'You profit {deposit - balance}₪ and {(balance - deposit) / get_dollar_rate()}$'

def get_loss(balance, deposit):
    return f'You loss {deposit - balance}₪ and {(deposit - balance) / get_dollar_rate()}$'
