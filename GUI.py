import tkinter as tk
from assignment_4b import fruits_and_vegetables


class MyGUI:

    def __init__(self):
        
        self.user_in = ""
        self.to_be_added = ""
        self.to_be_deleted = ""
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

        button_4 = tk.Button(buttonframe, text="Remove", command= self.gui_remove_from_list)
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

        self.input_field = tk.Entry(self.window)
        self.input_field.pack()
        self.ok_button = tk.Button(self.window, text="Search", command= self.start_search)
        self.ok_button.pack()
            
        self.user_in = self.input_field

    def start_search(self):

        self.user_in = self.user_in.get().strip()
        
        
        if self.user_in in fruits_and_vegetables:
            print("Found item")
            label2 = tk.Label(self.window, text="Found item: " + str(self.user_in))
            label2.pack()
                
        
        
        if  self.user_in not in fruits_and_vegetables and self.user_in != "":
            print("Item not found")
            label = tk.Label(self.window, text="Item: "+ str(self.user_in) + " was not found")
            label.pack()

        if  self.user_in == "":
            label = tk.Label(self.window, text="There is nothing to search with")
            label.pack()

        self.input_field.destroy()
        self.ok_button.destroy()
            

    def sort_list(self):
        fruits_and_vegetables_sorted = sorted(fruits_and_vegetables)
        label_list_sorted = tk.Label(self.window, wraplength=500,width=200,text=str(fruits_and_vegetables_sorted).translate(({ord(i): None for i in "[]''"})))
        label_list_sorted.pack()

    def show_list(self):
        label_list = tk.Label(self.window, wraplength=500,width=200,text=str(fruits_and_vegetables).translate(({ord(i): None for i in "[]''"})))
        label_list.pack()

    def add_to_list(self):
        
        self.input_field_add = tk.Entry()
        self.input_field_add.pack()

        self.to_be_added = self.input_field_add
       
        self.ok_button = tk.Button(self.window, text="Add item", command= self.append_list)
        self.ok_button.pack()

    def append_list(self):

        addition = self.to_be_added.get().strip()

        self.ok_button.destroy()
        self.input_field_add.destroy()

        if addition != "":
            fruits_and_vegetables.append(addition)
        
        if addition == "":
            no_add = tk.Label(text= "There is nothing to add")
            no_add.pack()
            
        self.ok_button.destroy()
        self.input_field_add.destroy()
        
    def gui_remove_from_list(self):

        self.to_be_deleted_in = tk.Entry()
        self.to_be_deleted_in.pack()

        self.to_be_deleted = self.to_be_deleted_in

        self.delete_button = tk.Button(text="Delete", command = self.remove_from_list)
        self.delete_button.pack()

    def remove_from_list(self):
        
        to_remove = self.to_be_deleted.get().strip()
        if to_remove in fruits_and_vegetables:
            fruits_and_vegetables.remove(to_remove)
            in_list = tk.Label(text="Item removed succesfully")
            in_list.pack()
        
        elif to_remove not in fruits_and_vegetables:
            not_in_list = tk.Label(text= "Item not in list")
            not_in_list.pack()

        self.delete_button.destroy()
        self.to_be_deleted_in.destroy()





        

        
        
    
        
        
        



MyGUI()

