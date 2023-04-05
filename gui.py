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
    n.config(width='10', height='10')
    n.config(bg=color)
    
filo0 = cajas_filo(4, 4, 'pink')
filo5 = cajas_filo(6, 2, 'yellow')
filo3 = cajas_filo(8, 3, 'yellow')
filo2 = cajas_filo(6, 6, 'gray')
filo4 = cajas_filo(8, 5, 'pink')
#marco_principal.config(width='1050', height='630')

ventana.mainloop()