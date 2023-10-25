import tkinter as tk
from assignment_4b import fruits_and_vegetables

class MyGUI:

    def __init__(self):
        
        """Defines window"""
        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.window.title("Listomator")

        """Defines label"""
        self.label = tk.Label(self.window, text = "Listomator")
        self.label.pack(padx = 10, pady = 10)
        """
        self.button = tk.Button(self.window, text = "test")
        self.button.pack()
        """

        """Functional buttonframe and buttons"""

        buttonframe = tk.Frame(self.window)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)


        button_1 = tk.Button(buttonframe, text="Stop Application", command = self.stop_app)
        button_1.grid(row=0, column=0, sticky="news")

        button_2 = tk.Button(buttonframe, text="Search", command = self.search_list)
        button_2.grid(row=0, column=1, sticky="news")

        button_3 = tk.Button(buttonframe, text="Add")
        button_3.grid(row=0, column=2, sticky="news")

        button_4 = tk.Button(buttonframe, text="Remove")
        button_4.grid(row=1, column=0, sticky="news")

        button_5 = tk.Button(buttonframe, text="Sort")
        button_5.grid(row=1, column=1, sticky="news")

        button_6 = tk.Button(buttonframe, text="List")
        button_6.grid(row=1, column=2, sticky="news")


        buttonframe.pack(fill='x')

        self.window.mainloop()

    def stop_app(self):
        
        self.window.destroy()

    def search_list(self):
        user_input = input("Search:")

        
        if user_input in fruits_and_vegetables:
            print("Found item")
            label2 = tk.Label(self.window, text="Found item")
            label2.pack()
                
        
        
        if user_input not in fruits_and_vegetables:
            print("Item not found")
            label = tk.Label(self.window, text="Item not found")
            label.pack()
MyGUI()

