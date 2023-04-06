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
        self.label1=ttk.Label(self.labelframe1, text="Desde fila:")
        self.label1.grid(column=0, row=0, padx=5, pady=5, sticky="e")
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5, sticky="e")
        

aplicacion1=Aplicacion() 