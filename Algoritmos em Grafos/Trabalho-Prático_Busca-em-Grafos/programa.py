import parse as par
import grafos as gr
import desenhar as des
import random as rand
import BFS
import Dijkstra as Dj

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

    ##G.listar_Prop()
    ## Teste de lista de adj: 
    #Inserindo arestas aleatórias -> Está funcionando.
    BFS.bfs(G, 1)
    for v in G.vertices:
        print(v.cor_p)
        if( v.pi != None):
            print(v.pi.nome)
        print(v.d)
        print()

    ##exibe_W(G)
    print(len(G.vertices))
    Dj.Dijkstra(G, 1)
    for v in G.vertices: 
        pai = v.pi
        print(f"{v.nome} - ", end = "")
        while pai != None: 
            print(f"{pai.nome} - ", end = "")
            pai = pai.pi
        print(f"Distância: {v.d}")
        print("\n")
    

    ##Teste de desenho: 
    des.desenhar(G)



def main():
    teste()



if __name__ == "__main__":
    main()