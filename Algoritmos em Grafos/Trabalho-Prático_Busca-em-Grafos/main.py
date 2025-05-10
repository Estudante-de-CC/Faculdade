import parse
import BFS

#inicializando grafo
Grafo = parse.obterDados()
Grafo.listar_Prop()

#lógica para propagação do fogo

#enquanto houver vértices com incêndio
tempo = 0
while Grafo.focos:

    print(f"\nno tempo {tempo}:")
    BFS.bfsMod(Grafo)
    
    tempo += 1


    