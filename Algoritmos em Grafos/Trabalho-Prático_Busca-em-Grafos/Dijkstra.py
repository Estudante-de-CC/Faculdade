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

def verificarAbastecimento(G, caminhao: caminhao):

    for foco in G.focos:
        if(caminhao.a_atual >= G.vertices[foco].qtdMaterialInflamavel):

            #possui quantidade de água necessária para apagar ao menos um foco
            return False
    
    #não tem água suficiente para apagar nenhum foco, logo precisa reabastecer
    return True


def alocarCaminhaoFoco(G, foco, brigadas, coletas):
    
    #itera pelas brigadas para verificar disponibilidade de equipes e caminhoes
    for brigada in brigadas:

        for caminhao in brigada.caminhoes:

            #obtendo vetor de caminho mínimo
            resultado = Dijkstra(G, caminhao.posicao.pos)

            for i, indicePai in enumerate(resultado[0]):
                G.vertices[i].pi = G.vertices[indicePai] if indicePai is not None else None

            #verificando necessidade de reabastecimento
            if not verificarAbastecimento(G, caminhao):
                
                if(caminhao.status == "disponivel" and caminhao.a_atual >= G.vertices[foco].qtdMaterialInflamavel):

                    #atribuindo foco ao caminhao disponível
                    caminhao.focoAtual = foco

                    #alterando status do caminhao
                    caminhao.alterarStatus("em_missao")

                    #reconstruindo caminho do caminhao disponível
                    reconstruirCaminho(G, caminhao, foco)

                    print(f"caminhao {caminhao.nome}")
                    print(f"com equipe {caminhao.equipe.nome} atribuída")
                    print(f"em missão ao foco {G.vertices[caminhao.focoAtual].nome}")
                    print(f"caminho ao foco: {caminhao.caminhoAoFoco}")

                    #Adicionando foco a lista de atendidos a fim de evitar que o mesmo seja alocado a dois
                    #ou mais caminhões distintos
                    G.focosAtendidos.append(foco)

                    return True
            
            else:
                
                if(caminhao.status == "disponivel"):

                    menorDistancia = inf
                    coletaMaisProxima = 0

                    #mudando status de caminhao
                    caminhao.alterarStatus("em_reabastecimento")

                    #iterando por todos os postos váidos de coleta incluíndo as próprias brigadas
                    for coleta in coletas:
                        if(resultado[1][coleta] < menorDistancia):
                            menorDistancia = resultado[1][coleta]
                            coletaMaisProxima = coleta

                    #atribuindo focoAtual como sendo o ponto mais próximo de coleta encontrado
                    caminhao.focoAtual = coletaMaisProxima
                    
                    reconstruirCaminho(G, caminhao, coletaMaisProxima)

                    print(f"caminhao {caminhao.nome} precisa reabastecer")
                    print(f"coleta mais próxima: {caminhao.focoAtual}")
                    print(f"caminho restante até coleta {caminhao.caminhoAoFoco}")
                    
        return False


def movimentarCaminhao(G, brigadas):
    
    for brigada in brigadas:
        for caminhao in brigada.caminhoes:

            #se caminhao estiver com status "em missão" e ainda tiver itens em sua
            #lista de caminho ao foco, removemos o primeiro elemento para simular a
            #movimentação em 1 vértice a cada turno
            
            if((caminhao.status == "em_missao" or caminhao.status == "em_reabastecimento") and caminhao.caminhoAoFoco):
                
                posicaoAtual = caminhao.caminhoAoFoco.pop(0)

                caminhao.n_pos(G.vertices[posicaoAtual])

                print(f"caminhao {caminhao.nome} andou 1 vertice em direação a {G.vertices[caminhao.focoAtual].nome}")
                print(f"caminho restante de {caminhao.nome} até {caminhao.focoAtual}: {caminhao.caminhoAoFoco}")

            #lista de caminhos de caminhao em missão está vazia então caminhao chegou ao foco e pode tratá-lo
            if(caminhao.status == "em_missao" and not caminhao.caminhoAoFoco):
                
                print(f"qtd água: [{caminhao.a_atual}] > qtd material inflamavel: [{G.vertices[caminhao.focoAtual].qtdMaterialInflamavel}]")
                
                caminhao.apagar(G.vertices[caminhao.focoAtual].qtdMaterialInflamavel)

                #decrementar quantidade de material inflamavel do foco
                G.vertices[caminhao.focoAtual].qtdMaterialInflamavel = 0

                #atualizando cor do foco atribuído ao caminhao
                G.vertices[caminhao.focoAtual].queimou()

                #removendo foco apagado da listagem de foco ativos
                G.focos.remove(caminhao.focoAtual)

                print(f"{caminhao.nome} apagou {G.vertices[caminhao.focoAtual].nome}")

                caminhao.alterarStatus("disponivel")
                caminhao.focoAtual = None
                caminhao.caminhoAoFoco = []

            #lista de caminhos de caminhao em reabastecimento está vazia então caminhao chegou a coleta e pode reabastecer
            if(caminhao.status == "em_reabastecimento" and not caminhao.caminhoAoFoco):
                caminhao.abastecer()
                print(f"caminhao {caminhao.nome} reabastecido [{caminhao.a_atual} L], posição {caminhao.posicao.nome}")

                #atribuir nova posição do caminhão ao local que ele reabasteceu

                caminhao.alterarStatus("disponivel")
                caminhao.focoAtual = None
                caminhao.caminhoAoFoco = []


def atualizarStatus(brigadas):

    for brigada in brigadas:
        for caminhao in brigada.caminhoes:

            if(not caminhao.caminhoAoFoco):

                #liberando caminhao
                caminhao.alterarStatus("disponivel")

def acaoBrigadistas(G):

    #ordenar focos com base na quantidade de vizinhos que possuem
    focos_ordenados = sorted(G.focos, key=lambda i: len(G.listas_adj[i]), reverse=True)
    #focos_ordenados = sorted(G.vertices, key=lambda v: len(v.listas_adj), reverse = True)

    #filtrar lista de vértices do grafo para apenas os que são brigadas
    brigadas = [v for v in G.vertices if v.tipo == 'b']

    #filtrar lista de vértices do grafo para apenas aos que são pontos válidos de coleta
    coletas = [v.pos for v in G.vertices if v.tipo == 'b' or v.tipo == 'c']

    #Atualizando disponibilidade das equipes e caminhões
    atualizarStatus(brigadas)

    #andando vértices no caminho até o foco para os caminhões que foram atrbibuidos em missões
    movimentarCaminhao(G, brigadas)

    #iterar por todos os focos ativos naquele turno priorizando os que possuem mais vizinhos
    for foco in focos_ordenados:
        if foco not in G.focosAtendidos:

            #alocando caminhao e equipes disponíveis aos focos ativos
            alocarCaminhaoFoco(G, foco, brigadas, coletas)








                




