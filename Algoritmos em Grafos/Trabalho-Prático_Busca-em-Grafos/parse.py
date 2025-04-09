#Leitura do arquivo com os parâmetros para execução do programa
import grafos as gf

def ler(): 
    with open('vertices.txt') as arquivo:
        for linha in arquivo:
            print(linha)
