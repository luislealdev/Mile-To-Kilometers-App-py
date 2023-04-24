from tkinter import *

def on_button_click():
    result_text["text"] = round(int(input.get())*1.60934, 2)


window = Tk()
window.title("Convert miles to kilometers")
window.minsize(width=500, height=500)
window.config(padx=50, pady=100)

input = Entry(width=10)
input.grid(column=1, row=0)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

equals_to_text = Label(text="is equals to")
equals_to_text.grid(column=0, row=1)

result_text = Label(text="0")
result_text.grid(column=1, row=1)

km_text = Label(text="Km")
km_text.grid(column=2, row=1)

button = Button(text="Calculate", command=on_button_click)
button.grid(column=1, row=2)


window.mainloop()
