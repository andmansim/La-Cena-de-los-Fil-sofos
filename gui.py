from tkinter import*


ventana = Tk()

#ventana.geometry('1050x630')
etiqueta = Label(ventana, text='La cena de los filósofos')
etiqueta.grid(column=1, row=0, pady = 5)


def cajas_filo(f,c, color):
    filo = Frame()
    filo.grid(row=f, column=c)
    filo.config(width='100', height='30')
    filo.config(bg=color)
    
def numeros(f, c, color):
    n =Frame()
    n.grid(row=f, column=c)
    n.config(width='15', height='15')
    n.config(bg=color)

def texto(f, c, palabra, dato) :
    
    dato = Label(ventana, text = palabra).grid(row=f, column=c)
filo0 = cajas_filo(4, 4, 'pink')
texto(4, 4, 'Filósofo 1', filo0)
filo5 = cajas_filo(6, 2, 'yellow')
texto(6, 2, 'Filósofo 5', filo5)
filo3 = cajas_filo(8, 3, 'yellow')
texto(8, 3, 'Filósofo 3', filo3)
filo2 = cajas_filo(6, 6, 'white')
texto(6, 6, 'Filósofo 2', filo2)
filo4 = cajas_filo(8, 5, 'pink')
texto(8, 5, 'Filósofo 4', filo4)

uno = numeros(4, 3, 'blue')
dos = numeros(5,5,'gray')
tres = numeros(7, 6, 'blue')
cuatro= numeros(8, 4, 'blue')
cinco= numeros(7, 2, 'blue')
#marco_principal.config(width='1050', height='630')

botsalir = Button(ventana, text='Salir')
botcreditos = Button(ventana, text='Créditos').grid(sticky= E)
botpausar = Button(ventana, text='Pausar').grid(sticky= E)
botiniciar= Button(ventana, text='Iniciar').grid(sticky= E)
botresert = Button(ventana, text='Resert').grid(sticky= E)
ventana.mainloop()