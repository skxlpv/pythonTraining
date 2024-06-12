from tkinter import *

window_width = 500
window_height = 500
button_width = 20
button_height = 2
label_width = 20
label_height = 2

main_window = Tk()
main_window.configure(bg='black')
main_window.title("Currency converter")
main_window.geometry("500x500")

root_canvas = Canvas(main_window, bg='red')
root_canvas.place(relx=.5, rely=.5, anchor=CENTER)
