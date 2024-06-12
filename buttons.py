from API_requests import fetch_one
from inputs import base, output, price, price_symbol, currency_amount
from root import *
from utils import symbols


def submit():
    currency_price = fetch_one(base.get(), output.get(), currency_amount.get())
    price.set(currency_price)
    symbol = str(symbols[output.get()])
    price_symbol.set(symbol)


fetch_button = Button(main_window, text='Fetch Price', command=submit, width=12, height=2)
