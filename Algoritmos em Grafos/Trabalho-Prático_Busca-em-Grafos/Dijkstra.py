import heap as HP
from math import inf

## LEGENDA -> 0 = PAI/CAMINHO
##         -> 1 = DISTÂNCIA EM SALTOS

def inicializar(G, ver):
    resultado = [[], []]
    for v in G.vertices:
        resultado[0].append(None)
        resultado[1].append(inf)
        if(v != ver):
            v.pai(None)
            v.dist(inf)
    resultado[1][G.vertices.index(ver)] = 0
    ver.pai(None)
    ver.d = 0
    return resultado

def init_HP(G, resultado):
    H = HP.heap()
    for v in G.vertices: 
        H.inserir(v, resultado[1][G.vertices.index(v)])
    return H
      
   
def relaxamento(G, H, u, v, resultado):

    if(resultado[1][G.vertices.index(v)] == (inf)): 
        medio  = 0
    else:
        medio  = resultado[1][G.vertices.index(v)]
    if (resultado[1][G.vertices.index(u)] > (medio + G.mat_custos[G.vertices.index(v)][G.vertices.index(u)])) and (u != v):
        aux = resultado[1][G.vertices.index(u)]
        resultado[1][G.vertices.index(u)] = medio + G.mat_custos[G.vertices.index(v)][G.vertices.index(u)]
        resultado[0][G.vertices.index(u)] = G.vertices.index(v)
        H.corrigir(u, aux, resultado[1][G.vertices.index(u)])
    

def exibir_H(H):
    for v in H.ordem:
        print(f"{v.ver.nome} - {v.prio}")

def Dijkstra(G, s):
    v = G.pos_ver(s)
    resultado = inicializar(G, v)
    H = init_HP(G, resultado)

    while (len(H.ordem) != 0):
        u = H.remover()
        adj = G.listas_adj[G.vertices.index(u)].raiz
        while (adj != None):
            relaxamento(G, H, adj.ver, u, resultado)
            adj = adj.next
        
    return resultado
        
    


