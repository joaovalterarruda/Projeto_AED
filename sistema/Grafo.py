import matplotlib.pyplot as plt
import itertools
import random
import json


class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = {}
        self.coordenadas = {}

    def adicionar_vertice(self, vertice, latitude, longitude):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}
            self.coordenadas[vertice] = (latitude, longitude)

    def remover_vertice(self, vertice):
        if vertice in self.vertices:
            del self.vertices[vertice]
            del self.coordenadas[vertice]
            for v in self.vertices:
                if vertice in self.vertices[v]:
                    del self.vertices[v][vertice]

    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem][destino] = True
            self.vertices[destino][origem] = True

    def remover_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices[origem]:
            del self.vertices[origem][destino]
            del self.vertices[destino][origem]

    def consultar_vertice(self, vertice):
        if vertice in self.vertices:
            return self.vertices[vertice]

    def consultar_coordenadas(self, vertice):
        if vertice in self.coordenadas:
            return self.coordenadas[vertice]

    def consultar_todos_vertices(self):
        return self.vertices.keys()

    def consultar_todas_arestas(self):
        return self.arestas.keys()


# Carregar os pontos do arquivo JSON
with open('pontos_interesse.json') as f:
    pontos = json.load(f)

# Criar o grafo e adicionar os vértices com as coordenadas
grafo = Grafo()
for ponto in pontos:
    designacao = ponto['designacao']
    latitude = ponto['latitude']
    longitude = ponto['longitude']
    grafo.adicionar_vertice(designacao, latitude, longitude)

# Gerar todas as combinações possíveis dos pontos
combinacoes = list(itertools.permutations(pontos))

# Selecionar aleatoriamente uma combinação
comb_selecionada = random.choice(combinacoes)

# Criar as arestas de acordo com a combinação selecionada
for i in range(len(comb_selecionada) - 1):
    origem = comb_selecionada[i]['designacao']
    destino = comb_selecionada[i + 1]['designacao']
    grafo.adicionar_aresta(origem, destino)


# Função para exibir o grafo
def exibir_grafo(grafo):
    fig, ax = plt.subplots()

    # Plotar os vértices
    for vertice in grafo.consultar_todos_vertices():
        coordenadas_vertice = grafo.consultar_coordenadas(vertice)
        ax.plot(coordenadas_vertice[1], coordenadas_vertice[0], 'bo')
        ax.annotate(vertice, (coordenadas_vertice[1], coordenadas_vertice[0]))

    # Plotar as arestas
    for origem in grafo.vertices:
        for destino in grafo.vertices[origem]:
            coordenadas_origem = grafo.consultar_coordenadas(origem)
            coordenadas_destino = grafo.consultar_coordenadas(destino)
            ax.plot([coordenadas_origem[1], coordenadas_destino[1]], [coordenadas_origem[0], coordenadas_destino[0]],
                    'b-')

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Grafo')

    plt.show()


# Exibir o grafo
exibir_grafo(grafo)
