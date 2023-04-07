import tkinter as tk
from tkinter import ttk

def patata(vent, f, c):
  a =  ttk.Entry( vent)
  a.grid(row=f, column=c)
  a.insert(0, 'aaa')
root = tk.Tk()
root.config(width=300, height=200)
entry1 = patata(root, 5, 5)
entry= ttk.Entry(root)
entry.place(x=50, y=50)
# Esta segunda caja de texto no puede recibir el foco
# vía la tecla Tab.
entry.insert(0, "Hola mundo!")
entry.place(x=50, y=50)
root.mainloop()