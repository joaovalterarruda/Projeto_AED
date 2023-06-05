import json
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#from LinkedList import LinkedList

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.adjacencias = {}

    def adicionar_vertice(self, nome, latitude, longitude):
        self.vertices[nome] = {'latitude': latitude, 'longitude': longitude}
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

    def desenhar_grafo(self):
        G = nx.DiGraph()  # Usar um grafo direcionado

        # Definir lista de cores
        cores = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan']

        for i, (vertice, posicao) in enumerate(self.vertices.items()):
            G.add_node(vertice, cor=cores[i % len(cores)])  # Atribuir uma cor diferente a cada vértice

        pos = {vertice: (posicao['longitude'], posicao['latitude']) for vertice, posicao in self.vertices.items()}

        for origem, adjacencias in self.adjacencias.items():
            for destino, peso in adjacencias:
                peso_arredondado = round(peso, 2)
                G.add_edge(origem, destino, weight=peso_arredondado)

        plt.figure(figsize=(12, 10))
        node_colors = [G.nodes[vertice]['cor'] for vertice in G.nodes]  # Obtém as cores dos vértices

        # Desenhar os nós
        nx.draw_networkx_nodes(G, pos, node_size=200, node_color=node_colors)

        # Desenhar as arestas com setas
        nx.draw_networkx_edges(G, pos, node_size=200,
                               edge_color='gray', width=1, arrowsize=15, arrowstyle='->')

        # Adicionar rótulos nas arestas
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

        # Adicionar rótulos nos nós
        nx.draw_networkx_labels(G, pos, font_size=1, font_color='black', font_weight='bold')

        # Criar legenda com rótulos dos vértices
        handles = [mpatches.Patch(color=color, label=vertice) for vertice, color in zip(G.nodes, node_colors)]
        plt.legend(handles=handles, title='Vértices', loc='upper right')

        plt.suptitle('Rede de Circulação: Ponta Delgada')  # Adicionar o título acima do gráfico

        plt.xlabel('Longitude')  # Adicionar legenda ao eixo x
        plt.ylabel('Latitude')  # Adicionar legenda ao eixo y

        plt.show()



# Carregar dados do arquivo JSON
with open('grafo.json') as json_file:
    dados = json.load(json_file)

# Criar instância da classe Grafo
grafo = Grafo()

# Adicionar vértices
for vertice in dados['vertices']:
    grafo.adicionar_vertice(vertice['nome'], vertice['latitude'], vertice['longitude'])

# Adicionar arestas
for aresta in dados['arestas']:
    grafo.adicionar_aresta(aresta['origem'], aresta['destino'], aresta['peso'])

# Exemplo de uso dos métodos
print("Lista de vértices:")
print(grafo.get_vertices())

print("Lista de arestas:")
print(grafo.get_arestas())

print("BFS:")
grafo.bfs('Portas do Mar')

print("DFS:")
grafo.dfs('Portas do Mar')

print("Dijkstra:")
distancias = grafo.dijkstra('Portas do Mar')
for vertice, distancia in distancias.items():
    print(f'Distância de Portas do Mar a {vertice}: {distancia}')

# Desenhar grafo
grafo.desenhar_grafo()
