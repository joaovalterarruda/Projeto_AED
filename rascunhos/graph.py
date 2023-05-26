import matplotlib.pyplot as plt
from projeto_aed.sistema.json import ler_ficheiro
from projeto_aed.sistema.constantes import FICHEIRO


class Graph:
    def __init__(self):
        self._vertices = {}
        self._edges = set()

    def add_vertex(self, vertex, attributes=None):
        if vertex not in self._vertices:
            self._vertices[vertex] = attributes if attributes is not None else {}
        else:
            raise ValueError("Vertex already exists in the graph.")

    def add_edge(self, source, target):
        if source in self._vertices and target in self._vertices:
            self._edges.add((source, target))
        else:
            raise ValueError("Source or target vertex does not exist in the graph.")

    def remove_vertex(self, vertex):
        if vertex in self._vertices:
            del self._vertices[vertex]
            self._edges = {(source, target) for (source, target) in self._edges if
                           source != vertex and target != vertex}
        else:
            raise ValueError("Vertex does not exist in the graph.")

    def remove_edge(self, source, target):
        edge = (source, target)
        if edge in self._edges:
            self._edges.remove(edge)
        else:
            raise ValueError("Edge does not exist in the graph.")

    def get_vertices(self):
        return list(self._vertices.keys())

    def get_edges(self):
        return list(self._edges)

    def map_network(self):
        data = ler_ficheiro(FICHEIRO)
        plt.figure(figsize=(16, 10))
        for ponto in data:
            designacao = ponto['designacao']
            latitude = ponto['latitude']
            longitude = ponto['longitude']
            self.add_vertex(designacao, {'latitude': latitude, 'longitude': longitude})
            plt.scatter(longitude, latitude, s=500, label=designacao)

        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('Rede de Circulação: Ponta Delgada')
        plt.legend()
        plt.show()
