import queue
from math import inf


def inicializa(G, ver):
   for v in G.vertices: 
      if(v != ver): 
         v.cor("Branco")
         v.dist(inf)
         v.pai(None)

   ver.pai(None)
   ver.d = 0
   ver.cor("Cinza")


def bfs(G , pos):
   s = G.pos_ver(pos)
   inicializa(G, s)
   Q = queue.Queue()
   Q.put(s)

   while (not(Q.empty())):
        u = Q.get()
        adj = G.listas_adj[G.vertices.index(u)].raiz

        while (adj != None):
           if (adj.ver.cor_p == "Branco"):
              adj.ver.cor("Cinza")
              adj.ver.dist(u.d + 1)
              adj.ver.pai(u)
              Q.put(adj.ver)
           adj = adj.next
        u.cor("Preto")
