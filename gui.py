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


#filosofo 2
filo2 = Frame()
filo2.grid(row=4, column=5)
filo2.config(width='100', height='30')
filo2.config(bg='white')

def cajas_filo(f,c, color):
    filo = Frame()
    filo.grid(row=f, column=f)
    filo.config(width='100', height='30')
    filo.config(bg=color)
    
filo= cajas_filo(4, 4, 'white')
filo0 = cajas_filo(4, 5, 'pink')
filo5 = cajas_filo(5, 3, 'yellow')
filoo = cajas_filo(5, 5, 'white')
filo2 = cajas_filo(5, 6, 'gray')
#marco_principal.config(width='1050', height='630')

ventana.mainloop()