import tkinter as tk

"""Defines window"""
window = tk.Tk()

window.geometry("500x500")
window.title("Listomator")

label = tk.Label(window, text="Listomator", font=('Arial', 18))
label.pack()

"""Buttons in window"""

buttonframe = tk.Frame(window)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

button_1 = tk.Button(buttonframe, text="1")
button_1.grid(row=0, column=0, sticky = "news")

button_2 = tk.Button(buttonframe, text="2")
button_2.grid(row=0, column=1, sticky = "news")

button_3 = tk.Button(buttonframe, text="3")
button_3.grid(row=0, column=2, sticky = "news")

button_4 = tk.Button(buttonframe, text="4")
button_4.grid(row=1, column=0, sticky = "news")

button_5 = tk.Button(buttonframe, text="5")
button_5.grid(row=1, column=1, sticky = "news")

button_6 = tk.Button(buttonframe, text="6")
button_6.grid(row=1, column=2, sticky = "news")



buttonframe.pack(fill = 'x')



window.mainloop()

