import random
import threading
import time

class Filosofo(threading.Thread):
    semaforo = threading.Lock()
    palillos= []
    estado = []
    num = 0
    def __init__(self):
        super().__init__()
        
        #atributos del problema
        self.id = Filosofo.num
        Filosofo.num +=1
        Filosofo.estado.append('pensando')
        Filosofo.palillos.append(threading.Semaphore(0)) #establece el semaforo del palillo de la izquierda
        print(f'Filósofo {self.id} está {Filosofo.estado[self.id]}')
   
   
    def pensar(self): 
        a = random.randint(0,5)
        time.sleep(a)
        print(f'El filósofo {self.id} está pensando {a}\t')
    
    def hambre(self):
        Filosofo.semaforo.acquire() #señala que tomará los palillos exclusión mutua
        Filosofo.estado[self.id] = 'hambriento'
        self.verificar(self.id) #Si no puede comer no se bloquea
        Filosofo.semaforo.release() #deja de señala que va a tomar los palillos
        Filosofo.palillos[self.id].acquire() #coge los palillos
        
    
    def verificar(self, a):
        a2 = a +1
        if a + 1 == 5:
            a2 =  0
        if Filosofo.estado[a] == 'hambriento' and Filosofo.estado[ a - 1] != 'comiendo' and Filosofo.estado[a2] != 'comiendo':
            Filosofo.estado[a] = 'comiendo'
            Filosofo.palillos[a].release() #aumenta el semáforo de los palillos
        
    def comer(self):
        print(f'Filosofo {self.id} está {Filosofo.estado[self.id]}')
        time.sleep(3)
        print(f'Filosofo {self.id} ha terminado de comer')
    
    def liberar(self):
        Filosofo.semaforo.acquire()
        Filosofo.estado[self.id] = 'pensando'
        self.verificar(self.id -1)
        self.verificar(self.id +1)
        Filosofo.semaforo.release()
        
    
    def run(self):
        while True:
            self.pensar()
            self.hambre()
            self.comer()
            self.liberar()


numfilosfos = 5

#primero ponemos a todos los filósofos a pensar y los guardamos en una lista para comprobar los estados
lista = []
for i in range (numfilosfos):
    lista.append(Filosofo())
for i in lista:
    #pasamos por cada filósofo para establecer un termpo de pensar, comer, etc.
    i.start()
 