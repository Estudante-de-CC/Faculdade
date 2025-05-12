import grafos as gr
import desenhar as des
import BFS
import Dijkstra as Dj
import Brigadas as Brigs

def insere_arb(G): 
    ## Quero tornar o insert fixo para evitar problemas futuros.
    ##Inserindo vértices
    for i in range (0, 14):
        if(i < 3):
              G.insere_ver('b')
        elif ((i >= 3) and (i < 10)):
              G.insere_ver('v')
        else:
              G.insere_ver('c')

    G.adc_lista_adj(1, 7, 4)
    G.adc_lista_adj(1, 8, 2)
    G.adc_lista_adj(2, 6, 9)
    G.adc_lista_adj(5, 6, 1)
    G.adc_lista_adj(5, 13, 2)
    G.adc_lista_adj(7, 5, 12)
    G.adc_lista_adj(0, 2, 16)
    G.adc_lista_adj(4, 13, 7)
    G.adc_lista_adj(9, 13, 12)
    G.adc_lista_adj(4, 9, 5)
    G.adc_lista_adj(9, 7, 17)
    G.adc_lista_adj(9, 11, 3)
    G.adc_lista_adj(10, 11, 1)
    G.adc_lista_adj(10, 3, 6)
    G.adc_lista_adj(0, 4, 6)
    G.adc_lista_adj(0, 8, 11)
    G.adc_lista_adj(0, 12, 9)
    G.adc_lista_adj(3, 12, 4)
    G.adc_lista_adj(12, 6, 9)

    ##Agora inserindo as arestas
    ##Nova Modificação - Quero remover os atributos de "pai", "cor" e etc. para colocar em outro lugar.

def exibe_W(G):
    P = G.mat_custos
    i = 1
    for v in P: 
        print(f"{i} + {v}")
        i +=1 


def teste():
    G = gr.grafo()
    insere_arb(G)

    print("Resultado de uma execução do algoritmo de BFS:")
    vetorBFS = BFS.bfs(G, 1)
    print(vetorBFS[0])
    print(vetorBFS[1])

    print()

    vetorDij = Dj.Dijkstra(G, 1)
    print("Resultado de uma execução do algoritmo de Dijkstra:")
    print(vetorDij[0])
    print(vetorDij[1])
    
    print()

    print("Caminho até o vértice: " + str(Brigs.caminho(G, 1, 12)))
   
    #des.desenhar(G)



def main():
    teste()



if __name__ == "__main__":
    main()