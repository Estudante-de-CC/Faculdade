import queue
import random
from math import inf


def inicializa(G, ver):
   resultado = [[], [], []]
   for v in G.vertices:
      resultado[0].append(None)
      resultado[1].append(inf)
      resultado[2].append("Branco")

   ver.pai(None)
   ver.d = 0
   ver.cor("Cinza")
   resultado[1][G.vertices.index(ver)] = 0
   resultado[2][G.vertices.index(ver)] = "Cinza"
   return resultado

def bfs(G , pos):
   s = G.pos_ver(pos)
   resultado = inicializa(G, s)
   Q = queue.Queue()
   Q.put(s)

   while (not(Q.empty())):
         u = Q.get()
         adj = G.listas_adj[G.vertices.index(u)].raiz

         while (adj != None):
            if (resultado[2][G.vertices.index(adj.ver)]== "Branco"):
               resultado[0][G.vertices.index(adj.ver)] = G.vertices.index(u)
               resultado[1][G.vertices.index(adj.ver)] = resultado[1][G.vertices.index(u)] + 1
               resultado[2][G.vertices.index(adj.ver)] = "Cinza"
               Q.put(adj.ver)
            adj = adj.next
         resultado[2][G.vertices.index(u)] = "Preto"
         u.cor("Preto")
   return resultado




#modificar BFS para não ser executado continuamente até todos os vértices serem marcados de preto
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


   #itera por uma cópia da lista de focos atuais (vértices incendiados remanescentes) a fim
   #de evitar perda de elementos iterados em decorrência da remoção dos focos
   for foco in G.focos[:]:

      #incendiado foco atual
      G.vertices[foco].fogo = True
      
      #acessa lista de adjacência do foco atual
      adj = G.listas_adj[foco].raiz.next

      print(f"foco atual: {G.vertices[foco].nome}, fogo -> {G.vertices[foco].fogo}")
      print(f"qtd material inflamável: {G.vertices[foco].qtdMaterialInflamavel}")
      print(f"qtd vizinhos: {len(G.listas_adj[foco])}; incendiados: {G.vertices[foco].qtdVizinhosIncendiados}")

      #itera por todos os vizinhos do foco analisado
      while(adj != None):

         #verifica se vizinho visitado através do foco atual é vegetação, e ainda não foi incendiado
         if(adj.ver.tipo == "v" and G.vertices[adj.ver.pos].fogo == False):

            #verifica se o vizinho já foi "incendiado" anteriormente
            if(G.vertices.index(adj.ver) not in G.focos):

               #calcula chance do fogo se propagar ao vizinho visitado
               chanceIncendio = 1 if random.random() <= probIncendio else 0

               print(f"tentativa para: {adj.ver.nome}; chance -> {chanceIncendio}")

               #incendeia vizinho e o adiciona aos focos
               if(chanceIncendio == 1):
                  print(f"adj fogo = {adj.ver.fogo}")

                  G.vertices[adj.ver.pos].fogo = True

                  G.focos.append(G.vertices.index(adj.ver))
                  G.vertices[foco].qtdVizinhosIncendiados += 1
                  
                  print(f"propagou para: {adj.ver.nome} \n")
                  print(G.focos)
   
         #prossegue ao próximo vizinho
         adj = adj.next
      
      #decremeta material inflamável de cada foco consumido pelo fogo em cada turno
      if(G.vertices[foco].qtdMaterialInflamavel > 0):

         #trantando do caso em que qtdMaterialInflamavel < qtdMaterialConsumido
         if(G.vertices[foco].qtdMaterialInflamavel < 200):
            qtdMaterialConsumido = G.vertices[foco].qtdMaterialInflamavel
         else:
            qtdMaterialConsumido = random.randint(100, 200)
            
         G.vertices[foco].qtdMaterialInflamavel -= qtdMaterialConsumido

      #removendo foco caso seu material inflamável tenha se esgotado
      if(G.vertices[foco].qtdMaterialInflamavel == 0):
         G.vertices[foco].queimou()
         G.focos.remove(foco)


#tratar questão dos vértices já queimados anteriormente retornando como foco depois [resolvido]
#verificar por que certos focos são pulados nos prints das  [resolvido]



