from tkinter import*


ventana = Tk()

#ventana.geometry('1050x630')
etiqueta = Label(ventana, text='La cena de los filósofos')
etiqueta.grid(column=1, row=0, pady = 5)

def cuadrado(filas, columnas, colores):
    c = Frame()
    c.grid(row=filas, column=columnas)
    c.config(width='10', height='20', bg = colores)



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

t = texto (5, 10, 'Código de colores:', None)
t1 = texto(12, 1, 'Log', None)
t2 = texto(13, 10, 'Cuántas veces han comido:', None)
rosa = cuadrado(6, 10, 'pink')
texto(6, 11, 'Filósofo entra a comer', None)
azul_c = cuadrado(7, 10, 'light blue')
texto(7, 11, 'Filósofo tiene un palillo', None)
naranja = cuadrado(8, 10, 'orange')
texto(8, 11, 'Filósofo está comiendo', None)
blanco = cuadrado(9, 10, 'white')
texto(9, 11, 'Está pensando', None)
azul_o =cuadrado(10, 10, 'blue')
texto(10, 11, 'Tenedor ocupado', None)
gris = cuadrado(11, 10, 'gray')
texto(11, 11, 'Tenedor libre', None)
#marco_principal.config(width='1050', height='630')

botsalir = Button(ventana, text='Salir')
botcreditos = Button(ventana, text='Créditos').grid(sticky= E)
botpausar = Button(ventana, text='Pausar').grid(sticky= E)
botiniciar= Button(ventana, text='Iniciar').grid(sticky= E)
botresert = Button(ventana, text='Resert').grid(sticky= E)
ventana.mainloop()