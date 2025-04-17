import grafos 
import vertice
import queue
from math import inf
 
def bfs(G, pos): 
    s = G.vertices[pos]
    for v in G.vertices: 
        if (v != s):
            v.cor_p = "Branco"
            v.distancia = float(inf)
            v.pai = None
    s.cor_p = "Cinza"
    s.distancia = 0
    s.pai = None
    Q = queue.Queue()
    Q.put(s)

    while(Q.qsize() != 0): 
        u = Q.get()
        print(type(u))
        l = G.listas_adj[G.vertices.index(u)].raiz
        while (l != None): 
            if (l.ver.cor_p == "Branco"):
                l.ver.cor_p = "Cinza"
                l.ver.dist = u.dist + 1
                l.ver.pai = u
                Q.put(l.ver)
            l = l.next
            
        u.cor_p = "Preto"
        