import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()

        self.framecopia()        
        self.ventana1.mainloop()


    def framecopia(self):
        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Region")
        self.labelframe1.grid(column=0, row=1, padx=5, pady=5, sticky="w")
        
      

        


    
        

aplicacion1=Aplicacion() 