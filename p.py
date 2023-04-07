from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext as st




class Gui():
    def __init__(self):
        pass
        
    
    def texto_grid(self, f, c, palabra, color, vent) :
        Label(vent, text = palabra, bg= color).grid(row=f, column=c)

    def texto_place(self, f, c, palabra, vent):
        ttk.Label(vent, text = palabra).place(x=f, y=c)

    def entry(self, f, c, vent) :
        a = ttk.Entry(vent)
        a.place(x = f, y = c)
        a.insert(0,'aaaa')
#textvariable=tipo,
    def boton(self, f, c, palabra, vent):
        ttk.Button(vent, text=palabra).grid(row=f, column=c)
        
    def block1(self):
        filo0 = Gui.texto_grid(4, 4, 'Filósofo 1', 'pink', cena)
        filo5 = Gui.texto_grid(6, 2, 'Filósofo 5', 'orange', cena)
        filo3 = Gui.texto_grid(8, 3, 'Filósofo 3', 'orange', cena)
        filo2 = Gui.texto_grid(6, 7, 'Filósofo 2', 'white', cena)
        filo4 = Gui.texto_grid(8, 5, 'Filósofo 4', 'pink', cena)
        #números
        uno = Gui.texto_grid(4, 3, '1', 'blue', cena)
        dos = Gui.texto_grid(5, 5, '2', 'gray', cena)
        tres = Gui.texto_grid(7, 6, '3', 'blue', cena)
        cuatro= Gui.texto_grid(8, 4, '4', 'blue', cena)
        cinco= Gui.texto_grid(7, 2, '5', 'blue', cena)

        t = Gui.texto_grid (3, 10, 'Código de colores:', None, cena)

        rosa = Gui.texto_grid(5, 10, None, 'pink', cena)
        fec= Gui.texto_grid(5, 11, 'Filósofo entra a comer', None, cena)
        azul_c = Gui.texto_grid(6, 10, None, 'light blue', cena)
        fp =Gui.texto_grid(6, 11, 'Filósofo tiene un palillo', None, cena)
        naranja = Gui.texto_grid(7, 10, None,'orange', cena)
        fc=Gui.texto_grid(7, 11, 'Filósofo está comiendo', None, cena)
        blanco = Gui.texto_grid(8, 10, None,'white', cena)
        fp=Gui.texto_grid(8, 11, 'Está pensando', None, cena)
        azul_o =Gui.texto_grid(9, 10,None, 'blue', cena)
        po=Gui.texto_grid(9, 11, 'Palillo ocupado', None, cena)
        gris = Gui.texto_grid(10, 10, None,'gray', cena)
        pl=Gui.texto_grid(10, 11, 'Palillo libre', None, cena)

    def block2(self):
        st.ScrolledText(l, width= 50, height = 10).grid(column=0, row=1, padx=5, pady=5)
        b = ttk.Label(l, text='Cuántas veces han comido:')
        b.grid(column=2, row=0, padx= 3, pady=3, sticky='e')
        f1 = Gui.texto_place(440, 30, 'Filósofo 1', l)
        f2= Gui.texto_place(440, 60, 'Filósofo 2', l)
        f3= Gui.texto_place(440, 90, 'Filósofo 3', l)
        f4= Gui.texto_place(440, 120, 'Filósofo 4', l)
        f5= Gui.texto_place(440, 150, 'Filósofo 5', l)

        e1 = Gui.entry(500, 30, l)
        e2 = Gui.entry(500, 60, l)
        e1 = Gui.entry(500, 90, l)
        e1 = Gui.entry(500, 120, l)
        e1 = Gui.entry(500, 150, l)
        
    def block3(self):
        crear_log= Checkbutton(c, text= 'Crear un log', variable= IntVar())
        crear_log.grid(column=0, row=2, padx=5, pady=5, sticky= 'w')

        botsalir = Gui.boton(1, 5, 'Salir', c)
        botcreditos = Gui.boton(2, 5, 'Créditos', c)
        botpausar = Gui.boton(2, 3,'Pausar',c)
        botiniciar= Gui.boton(2, 2, 'Iniciar', c)
        botresert = Gui.boton(2, 4,'Resert', c)


ventana = Tk() 
g = Gui()

cena= ttk.LabelFrame(ventana, text='La Cena de los Filósofos')
cena.grid(column=1, row=1, padx=5, pady=5, sticky= 'w')
g.block1

l= ttk.LabelFrame(ventana, text='Log')
l.grid(column=1, row=12, padx=5, pady=5, sticky= 'w')
g.block2
c= ttk.LabelFrame(ventana, text='Controles')
c.grid(column=1, row=14, padx=5, pady=5, sticky= 'w')
g.block3
ventana.mainloop()

'''
Falta pponer eltexto en las cajas de la Gui + Gui.botones
también que se vea como va sumando en esas cajitas y no solo el rsultado final. 
Lo de arrba e1.insert no funciona
'''