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
        Filosofo.estado.append('Pensando')
        Filosofo.palillos.append(threading.Semaphore(0)) #establece el semaforo del palillo de la izquierda
        
    def comer(self):
        print(f'El filósofo {self.numero} está comiendo') 
        
    def pensar(self):
        print(f'El filósofo {self.numero} está pensando')
    
    def Palilloiz(self):
        print(f'El filósofo {self.numero} obtiene el palillo izquierdo')
        print(f'Obtiene el palillo {self.numero}')
        #self.palillo[self.numero].acquire()
        Filosofo.lock.acquire()
    
    def Palillode(self):
        print(f'El filósofo {self.numero} obtiene el palillo derecho')
        self.palillo[self.temp].acquire()
    
    def liberaPaliz(self):
        print(f'El filósofo {self.numero} libera el palillo izquierdo')
        self.palillo[self.numero].release()
    
    def liberaPalde(self):
        print(f'El filósofo {self.numero} libera el palillo derecho')
        self.palillo[self.temp].release()
    
    def run(self):
        while True:
            self.pensar()
            self.Palilloiz()
            self.Palillode()
            self.comer()
            self.liberaPalde()
            self.liberaPaliz()

numfilosfos = 5


for i in range (0,4):
    t = Filosofo(i, palillos)
    t.start()
    time.sleep(0.5)