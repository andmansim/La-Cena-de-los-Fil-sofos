from tkinter import*
from tkinter import ttk, messagebox
from tkinter import scrolledtext as st
import random
import threading
import time
import ctypes
import os




class Filosofo(threading.Thread):
    semaforo = threading.Lock()
    palillos= []
    estado = []
    num = 0
    
    def __init__(self, tiempo):
        super().__init__()
        self.tiempo = tiempo
        #atributos del problema
        self.id = Filosofo.num
        Filosofo.num +=1
        self.vez_comer = 0
        Filosofo.estado.append('pensando')
        
        Filosofo.palillos.append(threading.Semaphore(0)) #establece el semaforo del palillo de la izquierda
        scrol.insert(INSERT,f'Filósofo {self.id} está {Filosofo.estado[self.id]} \n')
        print(f'Filósofo {self.id} está {Filosofo.estado[self.id]}')
        
   
    def control(self, d1, d2, d3, d4, d5):
        if self.id == 0:
            f = d1
        elif self.id == 1:
            f = d2
        elif self.id == 2:
            f = d3
        elif self.id == 3:
            f = d4
        elif self.id == 4:
            f = d5
        return f 
        
    
    def pensar(self): 
        a = random.randint(0,5)
        time.sleep(a)

    
    def hambre(self):
        Filosofo.semaforo.acquire() #señala que tomará los palillos exclusión mutua
        n = self.control(uno, dos, tres, cuatro, cinco)
        n.config(bg='gray')
            
        Filosofo.estado[self.id] = 'hambriento'
        f = self.control(filo1, filo2, filo3, filo4, filo5)
        f.config(bg='pink')
        self.verificar(self.id) #Si no puede comer no se bloquea
        Filosofo.semaforo.release() #deja de señala que va a tomar los palillos
        n = self.control(uno, dos, tres, cuatro, cinco)
        n.config(bg='light blue')
        Filosofo.palillos[self.id].acquire() #coge los palillos
        n = self.control(uno, dos, tres, cuatro, cinco)
        n.config(bg='blue')
  
    
    def verificar(self, a):
        if a == 5:
            a = 0
        a2 = a +1
        if a2 == 5:
            a2 =  0
        
        if Filosofo.estado[a] == 'hambriento' and Filosofo.estado[ a - 1] != 'comiendo' and Filosofo.estado[a2] != 'comiendo':
            Filosofo.estado[a] = 'comiendo'
            Filosofo.palillos[a].release() #aumenta el semáforo de los palillos
            n = self.control(uno, dos, tres, cuatro, cinco)
            n.config(bg='blue')

        
    def comer(self):
        print(f'Filosofo {self.id} está {Filosofo.estado[self.id]} \t')
        scrol.insert(INSERT,f'Filosofo {self.id} está {Filosofo.estado[self.id]} \n')
        f = self.control(filo1, filo2, filo3, filo4, filo5)
        f.config(bg='orange')
        e= self.control(e1, e2, e3, e4, e5)
        e.delete(0, 'end')
        self.vez_comer+=1
        e.insert(0, self.vez_comer)
        time.sleep(3)
        print(f'Filosofo {self.id} ha terminado de comer \t')
        f = self.control(filo1, filo2, filo3, filo4, filo5)
        f.config(bg='white')
    
        scrol.insert(INSERT,f'Filosofo {self.id} ha terminado de comer \n')
        

    def liberar(self):
        Filosofo.semaforo.acquire()
        n = self.control(uno, dos, tres, cuatro, cinco)
        n.config(bg='gray')
        Filosofo.estado[self.id] = 'pensando'
        
        self.verificar(self.id -1)
        self.verificar(self.id +1)
        Filosofo.semaforo.release()
        n = self.control(uno, dos, tres, cuatro, cinco)
        n.config(bg='light blue')
    
    def get_id(self):#cogemos el id del hilo para pararlo
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
    
    def raise_exception(self):
        thread_id = self.get_id()
        resu = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
        if resu > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
    
    def run(self):
        #for i in range(self.tiempo):
            
            self.pensar()
            self.hambre()
            self.comer()
            self.liberar()
            


def texto_grid( f, c, palabra, color, vent) :
    a = Label(vent, text = palabra, bg= color)
    a.grid(row=f, column=c)
    return a

def texto_place( f, c, palabra, vent):
    a = ttk.Label(vent, text = palabra)
    a.place(x=f, y=c)
    return a

    
def entry( f, c, vent) :
    a = ttk.Entry(vent)
    a.place(x = f, y = c)
    return a

def boton( f, c, palabra, vent):
    a = ttk.Button(vent, text=palabra)
    a.grid(row=f, column=c)
    return a


def empezar():
    botiniciar.config(state='disable')
   
    for i in range (numfilosfos):
        lista.append(Filosofo(tiempo))

    for i in lista:
        #pasamos por cada filósofo para establecer un termpo de pensar, comer, etc.
        i.start()

def parar1():
    botpausar.config(state='disable')
    for i in lista:
        i.raise_exception()

def resetear(): #Ns resetear
    for i in lista:
        i.raise_exception()
        
    for widget in l.winfo_children():
        if isinstance(widget, ttk.Entry):  # If this is an Entry widget 
            widget.delete(0,'end') # Delete all entries 
        
    #scrol.delete(, 'end')
    filo1.config(bg='white')
    filo2.config(bg='white')
    filo3.config(bg='white')
    filo4.config(bg='white')
    filo5.config(bg='white')
    uno.config(bg='gray')
    dos.config(bg='gray')
    tres.config(bg='gray')
    cuatro.config(bg='gray')
    cinco.config(bg='gray')
    os.system('cls')
    scrol.delete('1.0', 'end')
    lista.clear()
    Filosofo.num=0
    time.sleep(3)
    empezar()
    
def ventana_e():
    messagebox.showinfo('Créditos', 'Creado por: Andrea Manuel Simón')
      
def cerrar_ventana():
    ventana.destroy()

#Gráfica
ventana = Tk() 
ventana.title('La Cena de los Filósofos')
cena= ttk.LabelFrame(ventana, text='La Cena de los Filósofos')
cena.grid(column=1, row=1, padx=5, pady=5, sticky= 'w')

#Filósofos
filo1 = texto_grid(4, 4, 'Filósofo 1', 'white', cena)
filo5 = texto_grid(6, 2, 'Filósofo 5', 'white', cena)
filo3 = texto_grid(8, 3, 'Filósofo 3', 'white', cena)
filo2 = texto_grid(6, 7, 'Filósofo 2', 'white', cena)
filo4 = texto_grid(8, 5, 'Filósofo 4', 'white', cena)
#números
uno = texto_grid(4, 3, '1', 'gray', cena)
dos = texto_grid(5, 5, '2', 'gray', cena)
tres = texto_grid(7, 6, '3', 'gray', cena)
cuatro= texto_grid(8, 4, '4', 'gray', cena)
cinco= texto_grid(7, 2, '5', 'gray', cena)

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



#Programa
numfilosfos = 5
tiempo = 3
#primero ponemos a todos los filósofos a pensar y los guardamos en una lista para comprobar los estados
lista = []



#caja Log
l= ttk.LabelFrame(ventana, text='Log')
l.grid(column=1, row=12, padx=5, pady=5, sticky= 'w')
scrol = st.ScrolledText(l, width= 50, height = 10)
scrol.grid(column=0, row=1, padx=5, pady=5)
b = ttk.Label(l, text='Cuántas veces han comido:')
b.grid(column=2, row=0, padx= 3, pady=3, sticky='e')

f1 = texto_place(440, 30, 'Filósofo 1', l)
f2= texto_place(440, 60, 'Filósofo 2', l)
f3= texto_place(440, 90, 'Filósofo 3', l)
f4= texto_place(440, 120, 'Filósofo 4', l)
f5= texto_place(440, 150, 'Filósofo 5', l)

e1 = entry(500, 30, l)
e2 = entry(500, 60, l)
e3 = entry(500, 90, l)
e4 = entry(500, 120, l)
e5 = entry(500, 150, l)


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




botsalir.config(command=cerrar_ventana)
botiniciar.config(command=empezar)
botpausar.config(command= parar1)
botresert.config(command=resetear)
botcreditos.config(command=ventana_e)
ventana.mainloop()



