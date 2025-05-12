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
      
   
def relaxamento(G, H, u, v):
    if (v.d == (inf)):
        medio = 0
    else: 
        medio = v.d
    if (u.d > (medio + G.mat_custos[G.vertices.index(v)][G.vertices.index(u)])) and (u != v):
        aux = u.d
        u.dist(medio + G.mat_custos[G.vertices.index(v)][G.vertices.index(u)])
        u.pai(v)
        H.corrigir(u, aux, u.d)

def exibir_H(H):
    for v in H.ordem:
        print(f"{v.ver.nome} - {v.prio}")

def Dijkstra(G, s):
    v = G.pos_ver(s)
    inicializar(G, v)
    H = init_HP(G)

    while (len(H.ordem) != 0):
        u = H.remover()
        adj = G.listas_adj[G.vertices.index(u)].raiz
        while (adj != None):
            relaxamento(G, H, adj.ver, u)
            adj = adj.next
        
    


