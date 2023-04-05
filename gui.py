import tkinter as tk

'''
class Ventana(tk.Frame):
    def __init__(self, master = None):
        super(Ventana, self).__init__(master, width=1050, height=630)
        self.master.title('La Cena de los Filósofos')
        
        self.pack()
ventana = Ventana()
ventana.mainloop()'''

ventana = tk.Tk()
bot = tk.Button(ventana, text = 'NS', width = 25)
bot.grid(column=0, row = 0, padx = 5, pady=5 ) #posición 
ventana.mainloop()