from tkinter import*



ventana = Tk()

#ventana.geometry('1050x630')
etiqueta = Label(ventana, text='La cena de los filósofos')
etiqueta.grid(column=1, row=0, pady = 5)

#filosofo 1
filo1 = Frame()
filo1.grid(row=4, column=6)
filo1.config(width='100', height='30')
filo1.config(bg='pink')




#marco_principal.config(width='1050', height='630')

ventana.mainloop()