import grafos as Gr
import vertice 
import Dijkstra as dj
#Implementação do comportamento direto das brigadas.

'''Comportamento direto descrito - Ideias: 
    1 - Preciso do controle constante de quais vértices estão pegando fogo. -> Relação dos vértices
    em Focos e suas posições no vetor de vértices
    2 - Escolher o mais próximo para responder -> Desses vértices, escolha o com a menor distância em Dijkstra e vá até ele
    3 - Caminho até o vértice em questão: Fazer uma função que devolva o caminho para percorrer.
    4 - Fazer ua função que avance em um vértice a cada chamada até atingir o vértice em questão. Preciso manter sempre o caminho
    pra evitar que o caminhão fique fazendo voltas.
    Isso tudo deve ser colocado como atributo do caminhão?
'''

'''#Implementando -> 1: Vértices que estão queimando e suas posições
#   Você é um mapeamento, não precisa ser atributo de ninguém.
#   Vou voltar uma tupla no formato (vértice, índice)
   Eu preciso fazer 2 tipos de upgrade - Vértice incendiado e vértice normal.'''
def focos (grafo: Gr):
    
    pass


''' Implementando -> 2: Próxima escolha do mais próximo e cálculo do caminho.
        Nisso aqui, precisso pegar todos os caminhões das 3 brigadas. Mó trabalho
        Primeiro determinar que o algoritmo formule, de alguma maneira, o caminho até um determinado nó. O que já está feito.
        Agora, para fazer uma escolha, ele precisaria definir o vértice que planeja escolher...
'''

#Essa função me retorna um vetor com o caminho percorido de um determinado vértice até um outro determinado.
def caminho(G, inicio, objetivo, pais = None): 
    if pais == None:
        pais = dj.Dijkstra(G, inicio)
    retorno = []
    custo  = pais[1][objetivo]
    retorno.append(objetivo)
    while pais[0][objetivo] != None: 
        retorno.append(pais[0][objetivo])
        objetivo = pais[0][objetivo]
    print("Custo do caminho: " + str(custo))
    retorno.reverse()
    return retorno


'''Para essa parte de escolher os vetores, eu preciso pegar apenas os vetores de foco de incêndio, mas entra um problema
        Como fazer essa seleção de modo eficiente? E outra, preciso iterar por eles e pegar o de menor distância...
        Então, vou pegar os índices, analisar a matriz de distâncias de Dijkstra, coloco as distâncias todas em uma nova e pego a menor...
        O
'''
#Essa função deve escolher, entre os vetores que estão pegando fogo, o menor deles.
# Tá funcionando, aparentemente... 
# Se for pra retornar o caminho: 
def escolha(G, inicio, pais = None):
    pais = dj.Dijkstra(G, inicio)
    selecionar = []
    for v in G.focos:
        dist = pais[1][v]
        selecionar.append((v,dist)) 
    print(selecionar)
    if(selecionar != []):
        min(selecionar, key=lambda x : x[1])
        return(caminho(G, inicio,  min(selecionar, key=lambda x : x[1])[0]))
    else:
        return None
    

'''Implementando -> 4: Avançando de vértice em vértice até alcançar o caminho
'''
def proximo(): 
    pass

'''Fora movimentação, preciso de uma função para apagar o fogo também. Que, sinceramente, é a mais simples de se implementar.'''