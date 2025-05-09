import queue
import random
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

#modificar BFS para não se executado continuamente até todos os vértices serem marcados de preto
#mas sim para apenas iterar por todos os vizinhos de um dado vértice decidindo via probailidade fixa
#para cada vizinho se o mesmo vai ser incendiado

#havera uma lista geral em main contendo inicialmente apenas o vértice referente ao foco inicial do incêndio
#a medida que vértices vizinhos forem visitados a partir desse inicial os mesmos serão adicionados na fila

#a cada iteração visitaremos os vizinhos de todos os vértices da lista, de modo que um dado vértice
#vai ser removido da fila se todos os seus vizinhos já foram incendidados ou se ele já foi completamente
#queimado

#vertice.fogo = True -> incendiado (ainda pode ser considerado para a propagação)
#vetice.color = "black" -> quimado (não pode mais ser considerado para propagação)

#apenas vertices de vegetacao podem ser incendiados

probIncendio = 0.5

def bfsMod(G):

   #itera por todos os focos atuais (vértices incendiados remanescentes)
   for i, foco in enumerate(G.focos):

      #remove foco da lista geral se ele já tiver sido completamente queimado
      if(G.vertices[foco].color == "black" or G.vertices[foco].qtdVizinhosIncendiados == len(G.listas_adj[foco]) ):
         G.focos.remove(foco)
         continue
      
      #acessa lista de adjacência do foco atual
      adj = G.listas_adj[foco].raiz.next

      print(f"foco atual: {G.vertices[foco].nome}:")
      print(f"qtd vizinhos: {len(G.listas_adj[foco])}; incendiados: {G.vertices[foco].qtdVizinhosIncendiados}")

      #itera por todos os vizinhos do foco analisado
      while(adj != None):

         #verifica se vizinho visitado através do foco atual é vegetação, e ainda não foi incendiado
         if(adj.ver.tipo == "v" and adj.ver.fogo == False):

            #verifica se o vizinho já foi "incendiado" anteriormente
            if(G.vertices.index(adj.ver) not in G.focos):

               #calcula chance do fogo se propagar ao vizinho visitado
               chanceIncendio = 1 if random.random() <= probIncendio else 0

               print(f"tentativa para: {adj.ver.nome}; chance -> {chanceIncendio}")

               #incendeia vizinho e o adiciona aos focos
               if(chanceIncendio == 1):
                  adj.ver.fogo = True
                  G.focos.append(G.vertices.index(adj.ver))
                  G.vertices[foco].qtdVizinhosIncendiados += 1
                  
                  print(f"propagou para: {adj.ver.nome} \n")
                  print(G.focos)
            
         #prossegue ao próximo vizinho
         adj = adj.next


