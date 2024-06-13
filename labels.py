from frames import input_frame, price_frame
from inputs import base_currency_input, output_currency_input, price, amount_input, output, price_symbol, error
from buttons import fetch_button
from root import *


def create_labels():
    main_label = Label(main_window, text='Currency Convertor',
                       width=label_width, height=label_height,
                       bg='black', fg='white', font='Impact 20', pady=20)

    description_label = Label(main_window, text='Enter currency signs (USD, UAH, EUR)\nand amount to fetch price',
                              width=200, bg='black', fg='white', font="Halvatica 12", pady=10)

    price_label = Label(price_frame, textvariable=price,
                        height=label_height,
                        bg='black', fg='white', font='Impact 20')

    symbol_label = Label(price_frame, textvariable=price_symbol,
                         height=label_height,
                         bg='black', fg='white', font='Impact 20')

    from_to_label = Label(input_frame, text="----------------->",
                          height=3, justify='center',
                          bg='black', fg='white', font="Halvatica 12")

    error_label = Label(main_window, textvariable=error,
                        height=label_height, bg='black', fg='white',
                        font="Halvatica 10")

    main_label.pack()
    description_label.pack()

    base_currency_input.pack(side=LEFT, padx=20, pady=20)
    output_currency_input.pack(side=RIGHT, padx=20, pady=20)
    from_to_label.pack(anchor='se')

    input_frame.pack()

    amount_input.pack(pady=5)

    price_label.pack(side=RIGHT)
    symbol_label.pack(side=LEFT)

    fetch_button.pack(pady=10)

    price_frame.pack(padx=2)

    error_label.pack()
