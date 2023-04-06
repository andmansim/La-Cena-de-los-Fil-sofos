from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext as st
ventana = Tk()

def cuadrado(filas, columnas, colores):
    c = Frame()
    c.grid(row=filas, column=columnas)
    c.config(width='10', height='20', bg = colores)



def texto(f, c, palabra, color, vent) :
    Label(vent, text = palabra, bg= color).grid(row=f, column=c)

cena= ttk.LabelFrame(ventana, text='La Cena de los Filósofos')
cena.grid(column=1, row=1, padx=5, pady=5, sticky= 'w')

filo0 = texto(4, 4, 'Filósofo 1', 'pink', cena)
filo5 = texto(6, 2, 'Filósofo 5', 'orange', cena)
filo3 = texto(8, 3, 'Filósofo 3', 'orange', cena)
filo2 = texto(6, 6, 'Filósofo 2', 'white', cena)
filo4 = texto(8, 5, 'Filósofo 4', 'pink', cena)

uno = texto(4, 3, '1', 'blue', cena)
dos = texto(5, 5, '2', 'gray', cena)
tres = texto(7, 6, '3', 'blue', cena)
cuatro= texto(8, 4, '4', 'blue', cena)
cinco= texto(7, 2, '5', 'blue', cena)

t = texto (3, 9, 'Código de colores:', None, cena)

rosa = texto(6, 10, None, 'pink', cena)
fec= texto(6, 11, 'Filósofo entra a comer', None, cena)
azul_c = texto(7, 10, None, 'light blue', cena)
fp =texto(7, 11, 'Filósofo tiene un palillo', None, cena)
naranja = texto(8, 10, None,'orange', cena)
fc=texto(8, 11, 'Filósofo está comiendo', None, cena)
blanco = texto(9, 10, None,'white', cena)
fp=texto(9, 11, 'Está pensando', None, cena)
azul_o =texto(10, 10,None, 'blue', cena)
po=texto(10, 11, 'Palillo ocupado', None, cena)
gris = texto(11, 10, None,'gray', cena)
pl=texto(11, 11, 'Palillo libre', None, cena)


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