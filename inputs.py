from frames import input_frame
from root import *

base = StringVar()
output = StringVar()
price = StringVar()
price_symbol = StringVar()
currency_amount = IntVar()

base_currency_input = Entry(input_frame, textvariable=base, width=10, font='Impact 12', justify='center')
output_currency_input = Entry(input_frame, textvariable=output, width=10, font='Impact 12', justify='center')
amount_input = Entry(main_window, textvariable=currency_amount, width=10, font='Impact 12', justify='center')
