import parse as par
import grafos as gr
import desenhar as des
import random as rand

def testado(): 
    G = gr.grafo()
    ##Teste de vértices -> Inserir os vértices está funcionando. 
    G.insere_ver('b')
    G.insere_ver('b')
    G.insere_ver('b')
    G.insere_ver('v')
    G.insere_ver('c')

    G.listar_v()

    print(f"Qtd de vertices: {len(G.vertices)}")

    ## Teste de lista de adj: 
    #Inserindo arestas aleatórias -> Está funcionando.
    G.adc_lista_adj(0, 1, 4)
    G.adc_lista_adj(0, 2, 3)
    G.adc_lista_adj(0, 3, 8)
    G.adc_lista_adj(0, 3, 8) 
    G.adc_lista_adj(0, 4, 1)    

    G.adc_lista_adj(1, 0, 3)
    G.adc_lista_adj(1, 2, 5)
    G.adc_lista_adj(1, 4, 2)
    
    #Exibir arestas através da lista -> Está funcionando
    for a in G.listas_adj:
        a.Exibir_adj()
    
    ## Agora para a matiz de custos: --> Aparentemente funcional desde já. Amém!
    for i in G.mat_custos:
        print(len(i), end = '')
        print(i)

    print("Pós - Alterar: ")

    G.insere_ver('c')

    for i in G.mat_custos:
        print(len(i), end = '')
        print(i)
    
    print(f"Qtd de listas: {len(G.listas_adj)}")

    ##Teste de desenho: 
    des.desenhar(G)


def insere_arb(G): 
    qtd_vert = 20
    tipos = ['b', 'c', 'v']
    for i in range(qtd_vert):
        G.insere_ver(rand.choice(tipos))


    for i in range(len(G.vertices) + 4):
        no_1 = rand.randint(0, len(G.vertices)) - 1
        no_2 = rand.randint(0, len(G.vertices)) - 1
        if no_1 != no_2: 
            G.adc_lista_adj(no_1, no_2, rand.randint(0, 100)) 

def teste():
    G = gr.grafo()
    ##Teste de vértices -> Inserir os vértices está funcionando. 
    insere_arb(G)

    G.listar_Prop()
    ## Teste de lista de adj: 
    #Inserindo arestas aleatórias -> Está funcionando.
    

    ##Teste de desenho: 
    des.desenhar(G)



def main():
    teste()



if __name__ == "__main__":
    main()