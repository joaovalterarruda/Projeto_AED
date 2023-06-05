import json
import math
from typing import List

import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
from projeto_aed.sistema.json import ler_ficheiro
from projeto_aed.sistema.constantes import FICHEIRO
from projeto_aed.sistema.LinkedQueue import LinkedQueue


def criar_e_visualizar_grafo():
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
        sorted_points = sorted(data,
                               key=lambda p, designacao=designacao: distances.get((designacao, p['designacao']),
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






class Graph:
    def __init__(self):
        self._graph = nx.DiGraph()

    def __str__(self) -> str:
        return str(self._graph)

    def get_vertices(self) -> set[str]:
        return set(self._graph.nodes)

    def get_edges(self) -> set[tuple[str, str]]:
        return set(self._graph.edges)

    def adjacents(self, label: str) -> set[str]:
        return set(self._graph.neighbors(label))

    def add_vertex(self, label: str, attributes=None) -> None:
        self._graph.add_node(label, **(attributes or {}))

    def add_edge(self, from_label: str, to_label: str, weight: float) -> None:
        self._graph.add_edge(from_label, to_label, weight=weight)

    def breath_first_traversal(self, from_label: str) -> list[str]:
        return list(nx.bfs_tree(self._graph, from_label))

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

        nx.draw_networkx_edges(self._graph, pos, arrows=True)  # Desenhar as arestas com setas

        for (source, target), label in labels.items():
            x = (pos[source][0] + pos[target][0]) / 2  # Coordenada x média
            y = (pos[source][1] + pos[target][1]) / 2  # Coordenada y média
            plt.text(x, y, label, fontsize=12, ha='center', va='center')  # Exibir rótulo na posição média

        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('Rede de Circulação: Ponta Delgada')

        # Adicionar a legenda separada dos vértices
        legend_handles = []
        for i, group in enumerate(node_groups):
            legend_handles.append(
                plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=node_colors[i], markersize=10))
        plt.legend(legend_handles, node_groups, title='Grupos', loc='upper right')

        plt.show()


    def obter_caminhos_alternativos(self, ponto_inicial: str, ponto_final: str):
        """
        Procura todos os caminhos alternativos entre o ponto inicial e o ponto final, utilizando a travessia em largura
        :param ponto_inicial: ponto inicial
        :param ponto_final: ponto final
        :return: uma lista com os caminhos alternativos
        """
        caminhos = []
        caminhos_visitados = set()
        queue = LinkedQueue()
        queue.add([ponto_inicial])

        while not queue.is_empty():
            path = queue.pop()
            last_vertex = path[-1]

            if last_vertex == ponto_final:
                caminhos.append(path)

            if last_vertex not in caminhos_visitados:
                caminhos_visitados.add(last_vertex)
                adjacent_vertices = self.adjacents(last_vertex)
                for vertex in adjacent_vertices:
                    if vertex not in caminhos_visitados:
                        new_path = path + [vertex]
                        queue.add(new_path)

        return caminhos


    def interromper_via_circulacao(self, via_interrompida: str, ponto_inicial: str, ponto_final: str):
        """
        Encontrar os caminhos alternativos entre o ponto inicial e o ponto final, e remove do grafo
        :param via_interrompida: via interrompida
        :param ponto_inicial: ponto inicial
        :param ponto_final: ponto final
        :return: uma lista com os caminhos alternativos
        """
        # Faz uma copia do grafo original
        backup_grafo = Graph()
        for vertex in self.get_vertices():
            if vertex != via_interrompida:
                backup_grafo.add_vertex(vertex)

        for from_vertex, to_vertex in self.get_edges():
            if from_vertex != via_interrompida and to_vertex != via_interrompida:
                backup_grafo.add_edge(from_vertex, to_vertex)

        # Encontrar caminhos alternativos para o grafo
        caminhos_alternativos = self.obter_caminhos_alternativos(ponto_inicial, ponto_final)

        return caminhos_alternativos


    def interromper_via_circulacao_menu(self):
        via_interrompida = input("Informe a via de circulação a ser interrompida: ")
        ponto_inicial = input("Informe o ponto inicial: ")
        ponto_final = input("Informe o ponto final: ")

        caminhos_alternativos = self.interromper_via_circulacao(via_interrompida, ponto_inicial, ponto_final)
        print("Caminhos alternativos:")
        for caminho in caminhos_alternativos:
            print(caminho)