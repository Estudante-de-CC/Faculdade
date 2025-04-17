##Classes básicas relacionadas aos vértices usadas dentro do programa geral.

from math import inf
class vertice: 
    def __init__(self, tipo: chr, nome: str): 
        self.tipo = tipo
        self.nome = nome
        ### Para os algoritmos de busca: 
        self.dist = None
        self.pai = None
        self.cor_p = None

class caminhao:
    def __init__ (self, capacidade: int): 
        self.capacidade = capacidade
        self.a_atual = None
        self.posicao = None

    def n_pos(self, v: vertice):
        self.posicao = v

    def abastecer(self): 
        self.a_atual = self.capacidade

    def apagar(self, necessario: int):
        if self.a_atual >= necessario: 
            self.atual -= necessario
            return True
        return False


class brigada(vertice): 
    def __init__(self, caminhao: caminhao, qtd: int): 
        self.caminhao = caminhao
        self.qtd = qtd
        self.color = "red"

class vegetacao(vertice):
    def __init__(self):
        self.fogo: bool
        self.tempo = None
        self.color = "green"
    
    def queimou(self):
        self.color = "black"

class coleta(vertice): 
    def __init__(self):
        self.color = "blue"