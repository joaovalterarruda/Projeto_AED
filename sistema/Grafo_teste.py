import matplotlib.pyplot as plt


class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = {}

    def adicionar_vertice(self, latitude, longitude):
        vertice = (latitude, longitude)
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def remover_vertice(self, latitude, longitude):
        vertice = (latitude, longitude)
        if vertice in self.vertices:
            # Remove as arestas relacionadas ao vértice
            arestas = self.arestas.copy()
            for aresta in arestas:
                if vertice in aresta:
                    vertice_origem, vertice_destino = aresta
                    self.remover_aresta(vertice_origem[0], vertice_origem[1], vertice_destino[0], vertice_destino[1])

            # Remove o vértice
            del self.vertices[vertice]

    def adicionar_aresta(self, latitude_origem, longitude_origem, latitude_destino, longitude_destino):
        vertice_origem = (latitude_origem, longitude_origem)
        vertice_destino = (latitude_destino, longitude_destino)
        if vertice_origem in self.vertices and vertice_destino in self.vertices:
            aresta = (vertice_origem, vertice_destino)
            if aresta not in self.arestas:
                self.arestas[aresta] = True
                self.vertices[vertice_origem].append(vertice_destino)
                self.vertices[vertice_destino].append(vertice_origem)

    def remover_aresta(self, latitude_origem, longitude_origem, latitude_destino, longitude_destino):
        vertice_origem = (latitude_origem, longitude_origem)
        vertice_destino = (latitude_destino, longitude_destino)
        aresta = (vertice_origem, vertice_destino)
        if aresta in self.arestas:
            del self.arestas[aresta]
            self.vertices[vertice_origem].remove(vertice_destino)
            self.vertices[vertice_destino].remove(vertice_origem)

    def visualizar_grafo(self):
        plt.figure()
        for vertice, vizinhos in self.vertices.items():
            for vizinho in vizinhos:
                plt.plot([vertice[1], vizinho[1]], [vertice[0], vizinho[0]], 'k-')

        for vertice in self.vertices.keys():
            plt.plot(vertice[1], vertice[0], 'ro')
            plt.text(vertice[1], vertice[0], f'({vertice[0]}, {vertice[1]})', fontsize=8, verticalalignment='bottom')

        plt.show()


grafo = Grafo()

grafo.adicionar_vertice(-22.9068, -43.1729)
grafo.adicionar_vertice(-23.5505, -46.6333)
grafo.adicionar_vertice(51.5074, -0.1278)

grafo.adicionar_aresta(-22.9068, -43.1729, -23.5505, -46.6333)
grafo.adicionar_aresta(-23.5505, -46.6333, 51.5074, -0.1278)

grafo.visualizar_grafo()
