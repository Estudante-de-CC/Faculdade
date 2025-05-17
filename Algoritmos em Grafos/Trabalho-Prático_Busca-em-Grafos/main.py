import parse
import BFS
import Dijkstra

#inicializando grafo
Grafo = parse.obterDados()
Grafo.listar_Prop()

#enquanto houver vértices pegando fogo
tempo = 0
while Grafo.focos:

    print(f"\nTempo {tempo}:\n")

    print("Ação do fogo:")
    BFS.bfsMod(Grafo)

    print("\nAção dos brigadistas")
    Dijkstra.acaoBrigadistas(Grafo)
    
    tempo += 1

if(not Grafo.focos):
    print("incêndio conclúido \n")

    print("Relatório final da simulação: \n")

    if(len(Grafo.focosQueimados) > 0):
        print(f"tempo total da simualação: {tempo}")
    else:
        print(f"tempo necessário para conter fogo: {tempo} unidades de tempo") #[OK]

    print(f"quantidade de vértices totalmente queimados: {len(Grafo.focosQueimados)}") #[OK]
    print(f"quantidade de vértices salvos: {Grafo.qtdFocosSalvos}") #[OK]
    print(f"quantidade de equipes mobilizadas: {len(Grafo.equipesMobilizadas)}") #[OK]
    print(f"quantidade de reabastecimentos efetuados: {Grafo.reabastecimentos}") #[OK] 
    print(f"quantidade de água gasta: {Grafo.qtdAguaUtilizada}L") #[OK]



    