import random
import threading
import time

class Filosofo(threading.Thread):
    def __init__(self, numero, palillo):
        threading.Thread.__init__(self)
        #atributos del problema
        self.palillo = palillo
        self.numero = numero
        self.temp = self.numero + 1 % 5
    def comer(self):
        print(f'El filósofo {self.numero} está comiendo') 
        
    def pensar(self):
        print(f'El filósofo {self.numero} está pensando')
    
    def Palilloiz(self):
        print(f'El filósofo {self.numero} obtiene el palillo izquierdo')
        print(f'Obtiene el palillo {self.numero}')
        self.palillo[self.numero].acquire()
    
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
    