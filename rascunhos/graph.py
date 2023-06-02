import json
import math
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
from sistema.json import ler_ficheiro
from sistema.constantes import FICHEIRO


class Graph:
    def __init__(self):
        self._graph = nx.Graph()

    def add_vertex(self, vertex, attributes=None):
        self._graph.add_node(vertex, **(attributes or {}))

    def add_edge(self, source, target, weight):
        self._graph.add_edge(source, target, weight=weight)

    def get_weight(self, source, target):
        return self._graph[source][target]['weight']

    def map_network(self):
        pos = {vertex: (data['longitude'], data['latitude']) for vertex, data in self._graph.nodes(data=True)}
        labels = {(source, target): f"{data['weight']:.2f} km" for source, target, data in self._graph.edges(data=True)}

        plt.figure(figsize=(16, 10))

        node_groups = set([data.get('group', None) for node, data in self._graph.nodes(data=True)])
        node_colors = plt.cm.tab10.colors[:len(node_groups)]  # Cores para cada grupo de vértices

        for i, group in enumerate(node_groups):
            nodes = [node for node, data in self._graph.nodes(data=True) if data.get('group', None) == group]
            color = [node_colors[i]] * len(nodes)  # Lista de cores para os nós do grupo atual
            nx.draw_networkx_nodes(self._graph, pos, nodelist=nodes, node_color=color, node_size=800)

        nx.draw_networkx_labels(self._graph, pos)

        nx.draw_networkx_edges(self._graph, pos)
        nx.draw_networkx_edge_labels(self._graph, pos, edge_labels=labels, font_size=12)

        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('Rede de Circulação: Ponta Delgada')

        # Adicionar a legenda separada dos vértices
        legend_handles = []
        for i, group in enumerate(node_groups):
            legend_handles.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=node_colors[i], markersize=10))
        plt.legend(legend_handles, node_groups, title='Grupos', loc='upper right')

        plt.show()


# Criar instância do grafo
graph = Graph()

# Ler dados do arquivo JSON
data = list(ler_ficheiro(FICHEIRO))

# Adicionar vértices
for ponto in data:
    designacao = ponto['designacao']
    latitude = ponto['latitude']
    longitude = ponto['longitude']
    group = ponto.get('group', None)
    graph.add_vertex(designacao, {'latitude': latitude, 'longitude': longitude, 'group': group})

# Definir o número máximo de conexões por vértice
max_connections = 3

# Calcular distâncias entre todos os pares de pontos e armazenar em uma matriz
distances = {}
for ponto1, ponto2 in combinations(data, 2):
    distancia = math.dist((ponto1['latitude'], ponto1['longitude']), (ponto2['latitude'], ponto2['longitude']))
    distances[(ponto1['designacao'], ponto2['designacao'])] = distancia
    distances[(ponto2['designacao'], ponto1['designacao'])] = distancia

# Adicionar arestas com pesos até atingir o limite máximo de conexões
for ponto in data:
    designacao = ponto['designacao']
    if designacao not in graph._graph.nodes:
        continue

    # Ordenar os pontos de acordo com a distância do ponto atual
    sorted_points = sorted(data, key=lambda p, designacao=designacao: distances.get((designacao, p['designacao']),
                                                                                      float('inf')))

    # Adicionar arestas aos pontos mais próximos até atingir o limite máximo de conexões
    added_connections = 0
    for other_point in sorted_points:
        other_designacao = other_point['designacao']
        if other_designacao != designacao and other_designacao in graph._graph.nodes:
            graph.add_edge(designacao, other_designacao, distances[(designacao, other_designacao)])
            added_connections += 1

        if added_connections >= max_connections:
            break

# Mapear a rede e exibir o gráfico
graph.map_network()
