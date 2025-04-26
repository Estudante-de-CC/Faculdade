import heap as HP
from math import inf

def inicializar(G, ver):
   for v in G.vertices: 
        if(v != ver): 
            v.dist(inf)
            v.pai(None)

   ver.pai(None)
   ver.d = 0
def init_HP(G):
    H = HP.heap()
    for v in G.vertices: 
        H.inserir(v, v.d)
    return H
      
   
def relaxamento(G, u, v):
    if u.d >= v.d + G.mat_custos[G.vertices.index(v)][G.vertices.index(u)]:
        u.dist(v.d + G.mat_custos[G.vertices.index(v)][G.vertices.index(u)])

def exibir_H(H):
    for v in H.ordem: 
        print(f"{v.ver.nome} - {v.prio}")

def Dijkstra(G, s):
    v = G.pos_ver(s)
    inicializar(G, v)
    H = init_HP(G)
    H.remover()
    print(H.ultima())
    


