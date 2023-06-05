import json
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from projeto_aed.sistema.constantes import GRAFO


def desenhar_grafo(nome_arquivo):
    with open(nome_arquivo) as file:
        data = json.load(file)

    G = nx.DiGraph()

    cores = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan']

    # Adicionar vértices ao grafo
    for i, vertice in enumerate(data['vertices']):
        G.add_node(vertice['nome'], cor=cores[i % len(cores)])

    # Adicionar arestas ao grafo
    for aresta in data['arestas']:
        origem = aresta['origem']
        destino = aresta['destino']
        peso = aresta['peso']
        peso_arredondado = round(peso, 2)
        G.add_edge(origem, destino, weight=peso_arredondado)

    pos = {vertice['nome']: (vertice['longitude'], vertice['latitude']) for vertice in data['vertices']}

    plt.figure(figsize=(12, 10))
    node_colors = [G.nodes[vertice]['cor'] for vertice in G.nodes]
    nx.draw_networkx_nodes(G, pos, node_size=200, node_color=node_colors)
    nx.draw_networkx_edges(G, pos, node_size=200,
                           edge_color='gray', width=1, arrowsize=15, arrowstyle='->')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    nx.draw_networkx_labels(G, pos, font_size=1, font_color='black', font_weight='bold')
    handles = [mpatches.Patch(color=color, label=vertice) for vertice, color in zip(G.nodes, node_colors)]
    plt.legend(handles=handles, title='Vértices', loc='upper right')
    plt.suptitle('Rede de Circulação: Ponta Delgada')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()


# RF10 para testar
def testar_caminho():
    grafo = Grafo()
    origem = input("Digite o nome do ponto de partida: ")
    destino = input("Digite o nome do ponto de destino: ")
    caminhos_alternativos = grafo.encontrar_caminhos_alternativos(origem, destino)
    if caminhos_alternativos:
        print(f"\nCaminhos alternativos entre '{origem}' e '{destino}':")
        for caminho in caminhos_alternativos:
            print(" -> ".join(caminho))


# RF11
def obter_itinerario():
    grafo = Grafo()
    origem = input("Digite o nome do ponto de partida: ")
    destino = input("Digite o nome do ponto de destino: ")
    caminhos_alternativos = grafo.encontrar_caminhos_alternativos(origem, destino)
    if caminhos_alternativos:
        print(f"\nCaminhos alternativos entre '{origem}' e '{destino}':")
        for caminho in caminhos_alternativos:
            print(" -> ".join(caminho))

    distancia = grafo.dijkstra(origem)[destino]
    tempo_estimado_a_pe = distancia * 10  # Exemplo: 10 minutos por unidade de distância
    tempo_estimado_de_carro = distancia * 5  # Exemplo: 5 minutos por unidade de distância

    print(f"\nCaminho mais curto entre '{origem}' e '{destino}':")
    print(f"Distância a percorrer: {distancia} Km")
    print(f"Tempo estimado a pé: {tempo_estimado_a_pe} minutos")
    print(f"Tempo estimado de carro: {tempo_estimado_de_carro} minutos")

    desenhar_grafo(GRAFO)


class Grafo:
    def __init__(self):
        self.vertices = {}
        self.adjacencias = {}

    def adicionar_vertice(self, nome, latitude, longitude):
        self.vertices[nome] = (latitude, longitude)
        self.adjacencias[nome] = []

    def adicionar_aresta(self, origem, destino, peso):
        if origem != destino:  # Verificar se os vértices são diferentes
            if origem not in self.adjacencias[destino] and destino not in self.adjacencias[origem]:
                self.adjacencias[origem].append((destino, peso))

    def remover_vertice(self, nome):
        del self.vertices[nome]
        del self.adjacencias[nome]
        for adjacencias in self.adjacencias.values():
            adjacencias = [(v, p) for v, p in adjacencias if v != nome]

    def remover_aresta(self, origem, destino):
        if origem in self.adjacencias and destino in self.adjacencias[origem]:
            self.adjacencias[origem] = [(v, p) for v, p in self.adjacencias[origem] if v != destino]

    def get_vertices(self):
        return self.vertices.keys()

    def get_arestas(self):
        arestas = []
        for origem, adjacencias in self.adjacencias.items():
            for destino, peso in adjacencias:
                arestas.append((origem, destino, peso))
        return arestas

    def bfs(self, origem):
        visitados = set()
        fila = [origem]
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                print(vertice)
                visitados.add(vertice)
                for adjacente, _ in self.adjacencias[vertice]:
                    fila.append(adjacente)

    def dfs(self, origem):
        visitados = set()
        self._dfs_recursivo(origem, visitados)

    def _dfs_recursivo(self, vertice, visitados):
        visitados.add(vertice)
        print(vertice)
        for adjacente, _ in self.adjacencias[vertice]:
            if adjacente not in visitados:
                self._dfs_recursivo(adjacente, visitados)

    def dijkstra(self, origem):
        distancia = {v: float('inf') for v in self.vertices}
        distancia[origem] = 0
        visitados = set()

        while len(visitados) < len(self.vertices):
            vertice = min(
                {v: distancia[v] for v in self.vertices if v not in visitados},
                key=distancia.get
            )
            visitados.add(vertice)

            for adjacente, peso in self.adjacencias[vertice]:
                if adjacente not in visitados:
                    peso_total = distancia[vertice] + peso
                    if peso_total < distancia[adjacente]:
                        distancia[adjacente] = peso_total

        return distancia

    # RF10
    def interromper_via(self, origem, destino):
        if origem in self.adjacencias and destino in self.adjacencias[origem]:
            self.remover_aresta(origem, destino)
            caminhos_alternativos = self.encontrar_caminhos_alternativos(origem, destino)
            return caminhos_alternativos
        else:
            return []

    def encontrar_caminhos_alternativos(self, origem, destino):
        # Código para ler o JSON e adicionar vértices/arestas ao grafo
        with open(GRAFO) as json_file:
            dados = json.load(json_file)

        # Adicionar vértices
        for vertice in dados['vertices']:
            self.adicionar_vertice(vertice['nome'], vertice['latitude'], vertice['longitude'])

        # Adicionar arestas
        for aresta in dados['arestas']:
            self.adicionar_aresta(aresta['origem'], aresta['destino'], aresta['peso'])

        visitados = set()
        caminhos = []
        self._encontrar_caminhos_recursivo(origem, destino, [origem], caminhos, visitados)
        return caminhos

    def _encontrar_caminhos_recursivo(self, atual, destino, caminho, caminhos, visitados):
        if atual == destino:
            caminhos.append(caminho.copy())
        else:
            visitados.add(atual)
            for adjacente, _ in self.adjacencias[atual]:
                if adjacente not in visitados:
                    caminho.append(adjacente)
                    self._encontrar_caminhos_recursivo(adjacente, destino, caminho, caminhos, visitados)
                    caminho.pop()
            visitados.remove(atual)

# # Carregar dados do arquivo JSON
# with open('grafo.json') as json_file:
#     dados = json.load(json_file)
#
# # Criar instância da classe Grafo
# grafo = Grafo()
#
# # Adicionar vértices
# for vertice in dados['vertices']:
#     grafo.adicionar_vertice(vertice['nome'], vertice['latitude'], vertice['longitude'])
#
# # Adicionar arestas
# for aresta in dados['arestas']:
#     grafo.adicionar_aresta(aresta['origem'], aresta['destino'], aresta['peso'])

# # Exemplo de uso dos métodos
# print("Lista de vértices:")
# print(grafo.get_vertices())
#
# print("Lista de arestas:")
# print(grafo.get_arestas())
#
# print("BFS:")
# grafo.bfs('Portas do Mar')
#
# print("DFS:")
# grafo.dfs('Portas do Mar')
#
# print("Dijkstra:")
# distancias = grafo.dijkstra('Portas do Mar')
# for vertice, distancia in distancias.items():
#     print(f'Distância de Portas do Mar a {vertice}: {distancia}')
#
# # Desenhar grafo
# grafo.desenhar_grafo()
