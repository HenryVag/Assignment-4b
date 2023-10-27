import tkinter as tk
from assignment_4b import fruits_and_vegetables

class MyGUI:

    def __init__(self):
        
        self.user_in = ""
        self.to_be_added = ""
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

        button_3 = tk.Button(buttonframe, text="Add", command= self.add_to_list)
        button_3.grid(row=0, column=2, sticky="news")

        button_4 = tk.Button(buttonframe, text="Remove")
        button_4.grid(row=1, column=0, sticky="news")

        button_5 = tk.Button(buttonframe, text="Sort", command= self.sort_list)
        button_5.grid(row=1, column=1, sticky="news")

        button_6 = tk.Button(buttonframe, text="List", command=self.show_list)
        button_6.grid(row=1, column=2, sticky="news")


        buttonframe.pack(fill='x')

        self.window.mainloop()

    def stop_app(self):
        
        self.window.destroy()

    def search_list(self):

        input_field = tk.Entry(self.window)
        input_field.pack()
        ok_button = tk.Button(self.window, text="Search", command= self.start_search)
        ok_button.pack()
            
        self.user_in = input_field

    def start_search(self):

        user_in = self.user_in.get().strip()
        
        
        if user_in in fruits_and_vegetables:
            print("Found item")
            label2 = tk.Label(self.window, text="Found item: " + str(user_in))
            label2.pack()
                
        
        
        if  user_in not in fruits_and_vegetables:
            print("Item not found")
            label = tk.Label(self.window, text="Item: "+ str(user_in) + " was not found")
            label.pack()
            

        


    def sort_list(self):
        fruits_and_vegetables_sorted = sorted(fruits_and_vegetables)
        label_list_sorted = tk.Label(self.window, wraplength=500,width=200,text=str(fruits_and_vegetables_sorted).translate(({ord(i): None for i in "[]''"})))
        label_list_sorted.pack()

    def show_list(self):
        label_list = tk.Label(self.window, wraplength=500,width=200,text=str(fruits_and_vegetables).translate(({ord(i): None for i in "[]''"})))
        label_list.pack()

    def add_to_list(self):
        input_field_add = tk.Entry()
        input_field_add.pack()

        self.to_be_added = input_field_add
       
        ok_button = tk.Button(self.window, text="Add item", command= self.append_list)
        ok_button.pack()

    def append_list(self):

        addition = self.to_be_added.get().strip()
        fruits_and_vegetables.append(addition)
        

        

        
        
    
        
        
        



MyGUI()

