##Classes básicas relacionadas aos vértices usadas dentro do programa geral.

from math import inf

class vertice: 
    def __init__(self, tipo: chr, nome: str, pos: int): 
        self.tipo = tipo
        self.nome = nome
        self.pos = pos
        self.d = None
        self.pi = None
        self.cor_p = None
        self.explorados = 0

    def dist(self, dist): 
        self.d = dist
    def pai(self, ver): 
        self.pi = ver
    def cor(self, cor):
        self.cor_p = cor

class caminhao:
    def __init__ (self, capacidade: int): 
        self.capacidade = capacidade
        self.a_atual = None
        self.posicao = None
        self.status = "disponivel"
        self.caminhoAoFoco = []

    def n_pos(self, v: vertice):
        self.posicao = v

    def alterarStatus(self, status: chr):
        statusDisponiveis = ['disponivel', 'em_missao', 'em_reabastecimento']

        if(status in statusDisponiveis):
            self.status = status

    def abastecer(self): 
        self.a_atual = self.capacidade

    def apagar(self, necessario: int):
        if self.a_atual >= necessario: 
            self.atual -= necessario
            return True
        return False


class brigada(vertice): 
    def __init__(self,tipo: chr, nome: str, pos: int):
        super().__init__(tipo, nome, pos)
        self.caminhoes = []
        self.qtdEquipes = 0
        self.color = "red"

    def add_caminhoes(self, caminhoes: list):
            
        for veiculo in caminhoes:
            if(isinstance(veiculo, caminhao)):
                self.caminhoes.append(veiculo)
            else:
                print("caminhoes comporta apenas objetos do tipo caminhao")
    
    def add_equipes(self, qtd: int):
        self.qtdEquipes = qtd


class vegetacao(vertice):
    def __init__(self,tipo: chr, nome: str, pos: int):
        super().__init__(tipo, nome, pos)
        self.fogo = False
        self.tempo = None
        self.color = "green"
        self.qtdMaterialInflamavel = 0
        self.qtdVizinhosIncendiados = 0
        self.qtdVizinhosVegetacao = 0
    
    def queimou(self):
        self.color = "black"

    def contabilizarVegetacao(self, G):
        
        adj_temp = G.listas_adj[self.pos].raiz.next

        while adj_temp is not None:
            if adj_temp.ver.tipo == "v":
                self.qtdVizinhosVegetacao += 1
        
            adj_temp = adj_temp.next

class coleta(vertice): 
    def __init__(self,tipo: chr, nome: str, pos: int):
        super().__init__(tipo, nome, pos)
        self.color = "blue"