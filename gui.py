from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext as st
ventana = Tk()

def texto_grid(f, c, palabra, color, vent) :
    Label(vent, text = palabra, bg= color).grid(row=f, column=c)

def texto_place(f, c, palabra, vent):
    ttk.Label(vent, text = palabra).place(x=f, y=c)
    
cena= ttk.LabelFrame(ventana, text='La Cena de los Filósofos')
cena.grid(column=1, row=1, padx=5, pady=5, sticky= 'w')

#Filósofos
filo0 = texto_grid(4, 4, 'Filósofo 1', 'pink', cena)
filo5 = texto_grid(6, 2, 'Filósofo 5', 'orange', cena)
filo3 = texto_grid(8, 3, 'Filósofo 3', 'orange', cena)
filo2 = texto_grid(6, 7, 'Filósofo 2', 'white', cena)
filo4 = texto_grid(8, 5, 'Filósofo 4', 'pink', cena)
#números
uno = texto_grid(4, 3, '1', 'blue', cena)
dos = texto_grid(5, 5, '2', 'gray', cena)
tres = texto_grid(7, 6, '3', 'blue', cena)
cuatro= texto_grid(8, 4, '4', 'blue', cena)
cinco= texto_grid(7, 2, '5', 'blue', cena)

t = texto_grid (3, 11, 'Código de colores:', None, cena)

rosa = texto_grid(6, 10, None, 'pink', cena)
fec= texto_grid(6, 11, 'Filósofo entra a comer', None, cena)
azul_c = texto_grid(7, 10, None, 'light blue', cena)
fp =texto_grid(7, 11, 'Filósofo tiene un palillo', None, cena)
naranja = texto_grid(8, 10, None,'orange', cena)
fc=texto_grid(8, 11, 'Filósofo está comiendo', None, cena)
blanco = texto_grid(9, 10, None,'white', cena)
fp=texto_grid(9, 11, 'Está pensando', None, cena)
azul_o =texto_grid(10, 10,None, 'blue', cena)
po=texto_grid(10, 11, 'Palillo ocupado', None, cena)
gris = texto_grid(11, 10, None,'gray', cena)
pl=texto_grid(11, 11, 'Palillo libre', None, cena)


#caja Log
l= ttk.LabelFrame(ventana, text='Log')
l.grid(column=1, row=12, padx=5, pady=5, sticky= 'w')
st.ScrolledText(l, width= 50, height = 10).grid(column=0, row=1, padx=5, pady=5)
b = ttk.Label(l, text='Cuántas veces han comido:')
b.grid(column=2, row=0, padx= 3, pady=3, sticky='e')
f1 = texto_place(440, 30, 'Filósofo 1', l)
f2= texto_place(440, 60, 'Filósofo 2', l)
f3= texto_place(440, 90, 'Filósofo 3', l)
f4= texto_place(440, 120, 'Filósofo 4', l)
f5= texto_place(440, 150, 'Filósofo 5', l)
'''ttk.Label(l, text='Filósofo 1')
f1.place(x=440, y=30)'''
e1 = ttk.Entry(l, textvariable=StringVar())
e1.place(x=500, y = 30)
'''f2 = ttk.Label(l, text='Filósofo 2')
f2.place(x=440, y=60)'''
e2 = ttk.Entry(l, textvariable=StringVar())
e2.place(x=500, y = 60)
'''f3 = ttk.Label(l, text='Filósofo 3')
f3.place(x=440, y=90)'''
e3 = ttk.Entry(l, textvariable=StringVar())
e3.place(x=500, y = 90)
'''f4 = ttk.Label(l, text='Filósofo 4')
f4.place(x=440, y=120)'''
e4 = ttk.Entry(l, textvariable=StringVar())
e4.place(x=500, y = 120)
'''f5 = ttk.Label(l, text='Filósofo 5')
f5.place(x=440, y=150)'''
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