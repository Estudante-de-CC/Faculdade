import parse
import BFS
import Brigadas

#inicializando grafo
Grafo = parse.obterDados()
Grafo.listar_Prop()

#lógica para propagação do fogo

#enquanto houver vértices com incêndio
tempo = 0
while Grafo.focos:

    print(f"\nno tempo {tempo}:")
    BFS.bfsMod(Grafo)
    print(Brigadas.escolha(Grafo, 1))
    
    tempo += 1


    