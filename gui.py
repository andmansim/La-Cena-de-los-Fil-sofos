from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext as st

def texto_grid(f, c, palabra, color, vent) :
    Label(vent, text = palabra, bg= color).grid(row=f, column=c)

def texto_place(f, c, palabra, vent):
    ttk.Label(vent, text = palabra).place(x=f, y=c)


def entry(f, c, vent) :
    a = ttk.Entry(vent)
    a.place(x = f, y = c)
    a.insert(0,'aaaa')
#textvariable=tipo,
def boton(f, c, palabra, vent):
    ttk.Button(vent, text=palabra).grid(row=f, column=c)


ventana = Tk() 
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

t = texto_grid (3, 10, 'Código de colores:', None, cena)

rosa = texto_grid(5, 10, None, 'pink', cena)
fec= texto_grid(5, 11, 'Filósofo entra a comer', None, cena)
azul_c = texto_grid(6, 10, None, 'light blue', cena)
fp =texto_grid(6, 11, 'Filósofo tiene un palillo', None, cena)
naranja = texto_grid(7, 10, None,'orange', cena)
fc=texto_grid(7, 11, 'Filósofo está comiendo', None, cena)
blanco = texto_grid(8, 10, None,'white', cena)
fp=texto_grid(8, 11, 'Está pensando', None, cena)
azul_o =texto_grid(9, 10,None, 'blue', cena)
po=texto_grid(9, 11, 'Palillo ocupado', None, cena)
gris = texto_grid(10, 10, None,'gray', cena)
pl=texto_grid(10, 11, 'Palillo libre', None, cena)

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

e1 = entry(500, 30, l)
e2 = entry(500, 60, l)
e1 = entry(500, 90, l)
e1 = entry(500, 120, l)
e1 = entry(500, 150, l)

#caja controles

c= ttk.LabelFrame(ventana, text='Controles')
c.grid(column=1, row=14, padx=5, pady=5, sticky= 'w')

crear_log= Checkbutton(c, text= 'Crear un log', variable= IntVar())
crear_log.grid(column=0, row=2, padx=5, pady=5, sticky= 'w')

botsalir = boton(1, 5, 'Salir', c)
botcreditos = boton(2, 5, 'Créditos', c)
botpausar = boton(2, 3,'Pausar',c)
botiniciar= boton(2, 2, 'Iniciar', c)
botresert = boton(2, 4,'Resert', c)

'''for b in ej.lista:
    e1.insert(0, f'{ej.b.vez_comer}')
'''
ventana.mainloop()

'''
Falta pponer eltexto en las cajas de la Gui + botones
también que se vea como va sumando en esas cajitas y no solo el rsultado final. 
Lo de arrba e1.insert no funciona
'''