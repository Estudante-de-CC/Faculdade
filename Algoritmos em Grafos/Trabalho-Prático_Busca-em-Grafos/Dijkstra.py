import heap as HP
from math import inf
from vertice import caminhao

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

def reconstruirCaminho(G, cam: caminhao, foco: int):

    verticeAtual = G.vertices[foco]

    while verticeAtual != None and verticeAtual != cam.posicao:
        cam.caminhoAoFoco.insert(0, verticeAtual.pos)
        verticeAtual = verticeAtual.pi



#o que fará a função de deslocamento dos brigadistas

#após todo o processamento dos focos (incluindo propagação, consumo de material inflamável
#e queima por completo de um foco), os bombeiros teram em mãos uma lista de focos atuais
#correspondentes ao momento que se encontram (iteração atual)

#com base nisso eles devem considerar uma estratégia para direcionar suas equipes e caminhões
#aos focos mais adequados considerando fatores como qtd de equipes, qtd de caminhões e água 
#disponível nos caminhões, algumas possíveis estratégias são:

# se apenas um foco:
# ir diretamente ao mesmo

# se mais de um foco
# - ir diretamente aos focos com distancia mais curta em relação as brigadas direcionando as equipes e
#caminhões conforme disponibilidade
# - ir diretamente aos focos com maior perigo de propagação, ou seja, que possuem mais vizinhos de vegetação
# e portanto mais possibilidade de propagar

#OBS: mais de um foco pode ser tratado e analisado pelos brigadistas em um mesmo turno conforme disponibilidade
#de recursos (caminhões, equipes e água)

#como projetar a questão do deslocamento dos brigaditas?
# brigadistas se deslocam instataneamente, ou seja, chegam a um foco "escolhido" em um mesmo turno
#                   ou
# brigadistas se deslocam um vértice a cada turno até chegar no foco em questão


# como manipular os caminhões e as equipes de brigadistas?
# a cada turno após a escolha do foco, decrementa-se ou remove um dos objetos caminhões e quantidade de equipes
#em 1, após apagar o incêndio retornamos esse a quantidade de equipes original e o objeto de brigada mantido na
#do foco que apagaram


#como tratar a questão do reabastecimento?
#quando verificarmos que um objeto caminhão tem água_a igual a zero, fazemos o dijkstra para encontrar
#o caminho mais curto a todos os pontos de coleta, achado o ponto de coleta mais curto, direcionamos o
#caminhao ao mesmo e setamos sua água para a capacidade total

#lógica de apagar o fogo
#consideraremos que o fogo se apagado assim o será no mesmo turno que o caminhao chegar no foco
#se agua atual for >= a materialInflamavel o fogo será apagado por completo
#senao ainda tenho que decidir qual a alternativa mais lógica

def acaoBrigadistas(G):

    #ordenar focos com base na quantidade de vizinhos que possuem
    focos_ordenados = sorted(G.focos, key=lambda i: len(G.listas_adj[i]), reverse=True)
    #focos_ordenados = sorted(G.vertices, key=lambda v: len(v.listas_adj), reverse = True)

    #filtra lista de vértices do grafo para apenas os que são brigadas
    brigadas = [v for v in G.vertices if v.tipo == 'b']

    #iterar por todos os focos ativos naquele turno priorizando os que possuem mais vizinhos
    for foco in focos_ordenados:

        alocado = False

        if foco not in G.focosAtendidos:

            #iterar pelas brigadas para verificar a disponibilidade de suas equipes e caminhões
            for brigada in brigadas:
                for caminhao in brigada.caminhoes:
                    
                    #verifica disponibilidade do caminhão e se sua capacidade é suficiente para apagar o foco
                    if(caminhao.status == "disponivel" and caminhao.a_atual >= G.vertices[foco].qtdMaterialInflamavel):

                        #chama dijkstra para retornar o caminho mais curto enre o caminhao e o foco
                        resultado = Dijkstra(G, caminhao.posicao.pos)

                        for i, indicePai in enumerate(resultado[0]):
                            G.vertices[i].pi = G.vertices[indicePai] if indicePai is not None else None

                        #após isso terei a distancia do caminhao disponível em relação a todos os vértices

                        #reconstruindo caminho do caminhao disponível
                        reconstruirCaminho(G, caminhao, foco)

                        print(f"caminhao {caminhao} da brigada {G.vertices[brigada.pos].nome}")
                        print(f"em missão ao foco {G.vertices[foco].nome}")
                        print(f"caminho ao foco: {caminhao.caminhoAoFoco}")

                        #Adicionando foco a lista de atendidos a fim de evitar que o mesmo seja alocado a dois
                        #ou mais caminhões distintos
                        G.focosAtendidos.append(foco)
                        caminhao.alterarStatus("em_missao")
                        alocado = True

                        break

                if alocado == True:
                    break


                        #pra simular que o caminhao está andando até o foco posso a cada
                        #turno remover um elemento de sua lista caminhoAoFoco
                        #de modo que se a lista estiver vazia ele chegou ao foco e pode apagua-lo




                




