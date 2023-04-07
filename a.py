
from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext as st
from p import *
import ejercicio

#Programa
numfilosfos = 5
tiempo = 3
#primero ponemos a todos los filósofos a pensar y los guardamos en una lista para comprobar los estados
lista = []
for i in range (numfilosfos):
    lista.append(ejercicio.Filosofo(tiempo))
for i in lista:
    #pasamos por cada filósofo para establecer un termpo de pensar, comer, etc.
    i.start()


for a in lista:
    a.join()
    

for b in lista:
    print(b.id, b.vez_comer)



#Gráfica
ventana = Tk() 


cena= ttk.LabelFrame(ventana, text='La Cena de los Filósofos')
cena.grid(column=1, row=1, padx=5, pady=5, sticky= 'w')
block1(cena)
l= ttk.LabelFrame(ventana, text='Log')
l.grid(column=1, row=12, padx=5, pady=5, sticky= 'w')
block2(l ,2, 3, 4, 5, 6)
c= ttk.LabelFrame(ventana, text='Controles')
c.grid(column=1, row=14, padx=5, pady=5, sticky= 'w')
block3(c)

ventana.mainloop()
