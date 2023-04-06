from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext as st
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
filo5 = texto(6, 2, 'Filósofo 5', 'orange')
filo3 = texto(8, 3, 'Filósofo 3', 'orange')
filo2 = texto(6, 6, 'Filósofo 2', 'white')
filo4 = texto(8, 5, 'Filósofo 4', 'pink')

uno = texto(4, 3, '1', 'blue')
dos = texto(5, 5, '2', 'gray')
tres = texto(7, 6, '3', 'blue')
cuatro= texto(8, 4, '4', 'blue')
cinco= texto(7, 2, '5', 'blue')

t = texto (5, 10, 'Código de colores:', None)


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
#place(x=70, y= 250)

#Caja cena

#caja Log
l= ttk.LabelFrame(ventana, text='Log')
l.grid(column=1, row=12, padx=5, pady=5, sticky= 'w')
st.ScrolledText(l, width= 50, height = 10).grid(column=0, row=1, padx=5, pady=5)
b = ttk.Label(l, text='Cuántas veces han comido:')
b.grid(column=2, row=0, padx= 3, pady=3, sticky='e')
f1 = ttk.Label(l, text='Filósofo 1')
f1.place(x=440, y=30)
e1 = ttk.Entry(l, textvariable=StringVar())
e1.place(x=500, y = 30)
f2 = ttk.Label(l, text='Filósofo 2')
f2.place(x=440, y=60)
e2 = ttk.Entry(l, textvariable=StringVar())
e2.place(x=500, y = 60)
f3 = ttk.Label(l, text='Filósofo 3')
f3.place(x=440, y=90)
e3 = ttk.Entry(l, textvariable=StringVar())
e3.place(x=500, y = 90)
f4 = ttk.Label(l, text='Filósofo 4')
f4.place(x=440, y=120)
e4 = ttk.Entry(l, textvariable=StringVar())
e4.place(x=500, y = 120)
f5 = ttk.Label(l, text='Filósofo 5')
f5.place(x=440, y=150)
e5 = ttk.Entry(l, textvariable=StringVar())
e5.place(x=500, y = 150)



#caja controles

c= ttk.LabelFrame(ventana, text='Controles')
c.grid(column=1, row=14, padx=5, pady=5, sticky= 'w')

crear_log= Checkbutton(c, text= 'Crear un log', variable= IntVar())
crear_log.grid(column=0, row=2, padx=5, pady=5, sticky= 'w')

botsalir = ttk.Button(c, text='Salir').grid(column=5, row=1, padx=5, pady=5, sticky= 'e')
botcreditos = ttk.Button(c, text='Créditos').grid(column=5, row=2, padx=5, pady=5, sticky= 'w')
botpausar = ttk.Button(c, text='Pausar').grid(column=3, row=2, padx=5, pady=5, sticky= 'w')
botiniciar= ttk.Button(c, text='Iniciar').grid(column=2, row=2, padx=5, pady=5, sticky= 'w')
botresert = ttk.Button(c, text='Resert').grid(column=4, row=2, padx=5, pady=5, sticky= 'w')
ventana.mainloop()