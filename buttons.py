from API_requests import fetch_one
from inputs import base, output, price, price_symbol, currency_amount, error
from root import *
from utils import symbols
from _tkinter import TclError


def submit():
    try:
        base_value = base.get()
        output_value = output.get()
        currency_amount_value = currency_amount.get()

        currency_price = fetch_one(base_value, output_value, currency_amount_value)

        if currency_price is not None:
            try:
                price.set(currency_price)
                symbol = str(symbols[output.get()])
                price_symbol.set(symbol)
            except KeyError:
                pass
    except TclError:
        error.set("Please, provide correct amount of currency")
        currency_amount.set(0)


fetch_button = Button(main_window, text='Fetch Price', command=submit, width=12, height=2)
