from frames import main_frame
from root import *


def create_labels():
    main_label = Label(main_window, text='Currency Convertor',
                       width=label_width, height=label_height,
                       bg='black', fg='white', font=20)
    main_label.pack()
