from tkinter import*


ventana = Tk()

#ventana.geometry('1050x630')
etiqueta = Label(ventana, text='La cena de los filósofos')
etiqueta.grid(column=1, row=0, pady = 5)




def texto(f, c, palabra, color) :
    Label(ventana, text = palabra, bg= color).grid(row=f, column=c)
    
filo0 = texto(4, 4, 'Filósofo 1', 'pink')
filo5 = texto(6, 2, 'Filósofo 5', 'yellow')
filo3 = texto(8, 3, 'Filósofo 3', 'yellow')
filo2 = texto(6, 6, 'Filósofo 2', 'white')
filo4 = texto(8, 5, 'Filósofo 4', 'pink')

uno = texto(4, 3, '1', 'blue')
dos = texto(5, 5, '2', 'gray')
tres = texto(7, 6, '3', 'blue')
cuatro= texto(8, 4, '4', 'blue')
cinco= texto(7, 2, '5', 'blue')

#marco_principal.config(width='1050', height='630')

botsalir = Button(ventana, text='Salir')
botcreditos = Button(ventana, text='Créditos').grid(sticky= E)
botpausar = Button(ventana, text='Pausar').grid(sticky= E)
botiniciar= Button(ventana, text='Iniciar').grid(sticky= E)
botresert = Button(ventana, text='Resert').grid(sticky= E)
ventana.mainloop()