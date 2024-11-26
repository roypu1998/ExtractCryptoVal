from utils.declear import chat_id, my_balance_ils, get_profit, first_deposit, WEBHOOK_URL
from bot.bot import bot
from flask import Flask, request
from time import sleep
import threading
import os

app = Flask(__name__)


# הגדרת webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    if update:
        bot.process_new_updates([update])
    return "OK"


def run_flask():
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))


def run_main():
    print('main start')
    while True:
        if (my_balance_ils - first_deposit) > 500:
            bot.send_message(chat_id=chat_id, text=f'{get_profit(my_balance_ils, first_deposit)}')
        sleep(5)


if __name__ == '__main__':
    # הגדרת webhook עם Telegram
    bot.remove_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/webhook")

    # הרצת Flask ו-run_main באותה זמן באמצעות threading
    flask_thread = threading.Thread(target=run_flask)
    main_thread = threading.Thread(target=run_main)

    flask_thread.start()
    main_thread.start()
