#File name: gui.py
#Author: Henry Våg
#Description: Working GUI that can manipulate a list

import tkinter as tk
from list import fruits_and_vegetables


class MyGUI:

    def __init__(self):
        
        """Class variables"""
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

        """Separate frame for labels"""

        self.labelframe = tk.Frame(self.window, width=200, height=410)
        self.labelframe.pack(fill='x')

        self.window.mainloop()
    

    """Stops application"""
    def stop_app(self):
        
        self.window.destroy()

    """Gui for searhing in list"""
    def search_list(self):

        self.clear_labelframe()
        
        self.input_field = tk.Entry(self.labelframe)
        self.input_field.pack()
        self.ok_button = tk.Button(self.labelframe, text="Search", command= self.start_search)
        self.ok_button.pack()
            
        self.user_in = self.input_field
    
    """Executes search"""
     def start_search(self):

            
        self.user_in = self.user_in.get().strip()
        
        if 1 <= len(self.user_in) <= 25 :
        
            if self.user_in in fruits_and_vegetables:
                print("Found item")
                label2 = tk.Label(self.labelframe, text="Found item: " + str(self.user_in))
                label2.pack()
                    
            
            
            if  self.user_in not in fruits_and_vegetables and self.user_in != "":
                print("Item not found")
                label = tk.Label(self.labelframe, text="Item: "+ str(self.user_in) + " was not found")
                label.pack()

        if  self.user_in == "":
            label = tk.Label(self.labelframe, text="There is nothing to search with")
            label.pack()
        
        if len(self.user_in) >= 26:
            in_char = tk.Label(self.labelframe, text= "Incorrect amount of characters")
            in_char.pack()

        self.input_field.destroy()
        self.ok_button.destroy()
            
    """Sorts list alphabetically"""
    def sort_list(self):

        self.clear_labelframe()

        fruits_and_vegetables_sorted = sorted(fruits_and_vegetables)
        label_list_sorted = tk.Label(self.labelframe, wraplength=500,width=200,text=str(fruits_and_vegetables_sorted).translate(({ord(i): None for i in "[]''"})))
        label_list_sorted.pack()

    """Displays list"""
    def show_list(self):

        self.clear_labelframe()

        label_list = tk.Label(self.labelframe, wraplength=500,width=200,text=str(fruits_and_vegetables).translate(({ord(i): None for i in "[]''"})))
        label_list.pack()

    """Gui for adding element to list, only letters allowed"""
    def add_to_list(self):

        self.clear_labelframe()
        
        self.input_field_add = tk.Entry(self.labelframe)
        self.input_field_add.pack()

        self.to_be_added = self.input_field_add
       
        self.ok_button = tk.Button(self.labelframe, text="Add item", command= self.append_list)
        self.ok_button.pack()

    """Adds element to list if input is only letters"""
    def append_list(self):

        addition = self.to_be_added.get().strip()

        self.ok_button.destroy()
        self.input_field_add.destroy()

        additionlen = len(addition)
        if 1 <= additionlen <= 25 and addition.isalpha() == True:
            if addition != "" and (additionlen <= 25):
                fruits_and_vegetables.append(addition)
                added = tk.Label(self.labelframe,text= "Added "+str(addition)+" succesfully")
                added.pack()
            
        if addition == "":
            no_add = tk.Label(text= "There is nothing to add")
            no_add.pack()
        
        if addition.isalpha() == False:
            in_char = tk.Label(self.labelframe, text= "Incorrect amount or type of characters")
            in_char.pack()
        
        self.ok_button.destroy()
        self.input_field_add.destroy()

    """Gui for removing element from list""" 
    def gui_remove_from_list(self):

        self.clear_labelframe()

        self.to_be_deleted_in = tk.Entry(self.labelframe)
        self.to_be_deleted_in.pack()

        self.to_be_deleted = self.to_be_deleted_in

        self.delete_button = tk.Button(self.labelframe,text="Delete",command = self.remove_from_list)
        self.delete_button.pack()

    """Removes element from list"""
    def remove_from_list(self):
        
        to_remove = self.to_be_deleted.get().strip()

        if 1 <= len(to_remove) <= 25:
            if to_remove in fruits_and_vegetables:
                fruits_and_vegetables.remove(to_remove)
                in_list = tk.Label(self.labelframe, text="Item removed succesfully")
                in_list.pack()
            
            elif to_remove not in fruits_and_vegetables:
                not_in_list = tk.Label(self.labelframe, text= "Item not in list")
                not_in_list.pack()
        else:
            in_char = tk.Label(self.labelframe,text= "Incorrect amount of characters, please try again")
            in_char.pack()

        self.delete_button.destroy()
        self.to_be_deleted_in.destroy()

    """Clears labelframe, used at the start of every function if labelframe =! empty"""
    def clear_labelframe(self):
        if  self.labelframe != None:
            for item in self.labelframe.winfo_children():
                item.destroy()





        

        
        
    
        
        
        



MyGUI()

