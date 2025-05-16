import parse
import BFS
import Dijkstra

#inicializando grafo
Grafo = parse.obterDados()
Grafo.listar_Prop()

#lógica para propagação do fogo

#enquanto houver vértices com incêndio
tempo = 0
while Grafo.focos:

    print(f"\nTempo {tempo}:\n")

    print("Ação do fogo:")
    BFS.bfsMod(Grafo)

    print("\nAção dos brigadistas")
    Dijkstra.acaoBrigadistas(Grafo)
    
    tempo += 1

if(not Grafo.focos):
    print("incêndio conclúido")


    