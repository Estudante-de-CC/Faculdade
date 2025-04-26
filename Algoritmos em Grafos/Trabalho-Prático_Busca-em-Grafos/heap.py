import grafos as gr
import vertice as v
import linkedlist as list
import math as mt

class no: 
    def __init__(self, ver):
        self.ver = ver
        self.prio = None

    def set_prio(self, val):
        self.prio = val

class heap: 
    def __init__(self):
        self.ordem = [] 
    
    def inserir(self, ver, prio):
        x = no(ver)
        x.set_prio(prio)
        self.ordem.append(x)
        subir(self, self.ultima())

    def remover(self):
        if (len(self.ordem) > 0):
            x = self.ordem.pop(0)
            return x

    def ultima(self): 
        return (len(self.ordem) - 1)

        
def subir(H,i):
    j = mt.floor(i/2)
    if j >= 0:
        if H.ordem[i].prio < H.ordem[j].prio:
            temp = H.ordem[i]
            H.ordem[i] = H.ordem[j]
            H.ordem[j] = temp
            subir(H, j)

def descer(H, i):
    n = len(H.ordem)
    j = 2*i
    if j <= n: 
        if j < n: 
            if (H.ordem[j + 1].prio < H.ordem[j].prio):
                j = j+1
            if( H.ordem[i].prio > H.ordem[j].prio ):
                temp = H.ordem[i]
                H.ordem[i] = H.ordem[j]
                H.ordem[j] = temp
                descer(H, j)
