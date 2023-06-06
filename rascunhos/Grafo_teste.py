import json
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from projeto_aed.sistema.constantes import GRAFO


def desenhar_grafo(nome_arquivo):
    """
    Desenha o grafo a partir de um determinado ficheiro json
    :param nome_arquivo: Nome do ficheiro json
    :return:
    """
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
    """
    Input para testar o caminho alternativo
    :return:
    """
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
    """
    Obter inforomaçoes sobre o itenerário entre os dois pontos
    :return:
    """
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

    grafo.desenhar_grafo()


def obter_arvore_rotas_carro(ponto_interesse):
    """
    Obtém a subarvore de caminhos a partir de um ponto de interesse
    :param ponto_interesse: Ponto onde a árvore de caminhos de carro será obtida
    :return:
    """
    grafo = Grafo()

    # Adicionar vértices e arestas ao grafo
    with open(GRAFO) as json_file:
        dados = json.load(json_file)

    for vertice in dados['vertices']:
        grafo.adicionar_vertice(vertice['nome'], vertice['latitude'], vertice['longitude'])

    for aresta in dados['arestas']:
        grafo.adicionar_aresta(aresta['origem'], aresta['destino'], aresta['peso'])

    # Obter árvore de caminhos de carro a partir do ponto de interesse
    arvore = nx.DiGraph()
    visitados = set()
    visitados.add(ponto_interesse)
    obter_subarvore_carro(grafo, arvore, ponto_interesse, visitados)

    # Desenhar a árvore
    desenhar_arvore(arvore)


def obter_subarvore_carro(grafo, arvore, vertice, visitados):
    """
    Obtém a subarvore de caminhos de carro a partir de um vértice do grafo
    :param grafo: Grafo pela qual vai ser obtido a subarvore
    :param arvore: Subarvore de caminhos que está a ser construida
    :param vertice: Vértice onde a pesquisa é realizada
    :param visitados: Conjunto de vértices já visitados
    :return:
    """
    for adjacente, _ in grafo.adjacencias[vertice]:
        if adjacente not in visitados:
            visitados.add(adjacente)
            arvore.add_edge(vertice, adjacente)
            obter_subarvore_carro(grafo, arvore, adjacente, visitados)


def desenhar_arvore(arvore):
    """
    Desenha um grafo que representa a árvore de um grafo
    :param arvore:
    :return:
    """
    G = nx.DiGraph()

    cores = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan']

    # Adicionar vértices ao grafo
    for i, vertice in enumerate(arvore.nodes):
        G.add_node(vertice, cor=cores[i % len(cores)])

    # Adicionar arestas ao grafo
    for origem, destino in arvore.edges:
        peso = arvore[origem][destino].get('weight', 1)  # Obtém o peso ou usa 1 como valor padrão
        peso_arredondado = round(peso, 2)
        G.add_edge(origem, destino, weight=peso_arredondado)

    pos = nx.spring_layout(G)

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
    plt.suptitle('Rotas de percursos de carro:')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()


class Grafo:
    def __init__(self):
        self.vertices = {}
        self.adjacencias = {}

    def adicionar_vertice(self, nome, latitude, longitude):
        """
        Adiciona um vértice ao grafo com as coordenadas de latitude e longitude
        :param nome:
        :param latitude:
        :param longitude:
        :return:
        """
        self.vertices[nome] = (latitude, longitude)
        self.adjacencias[nome] = []

    def adicionar_aresta(self, origem, destino, peso):
        """
        Adiciona uma aresta ao grafo, ligando os dois vértices com um determinado peso
        :param origem: Nome do vértice de origem
        :param destino: Nome do vértice de destino
        :param peso: O peso da aresta
        :return:
        """
        if origem != destino:  # Verificar se os vértices são diferentes
            if origem not in self.adjacencias[destino] and destino not in self.adjacencias[origem]:
                self.adjacencias[origem].append((destino, peso))

    def calcular_centralidade_grau_interno(self, vertice):
        """
        Calculo do grau de centralidade interno de um vértice
        :param vertice:  Nome do vértice
        :return:
        """
        grau_interno = len(self.adjacencias[vertice])
        return grau_interno

    def calcular_centralidade_grau_externo(self, vertice):
        """
        Calculo do grau de centralidade extreno de um vértice
        :param vertice: Nome do vértice
        :return:
        """
        grau_externo = 0
        for v in self.vertices:
            if v != vertice:
                if any(aresta[0] == vertice for aresta in self.adjacencias[v]):
                    grau_externo += 1
        return grau_externo

    def calcular_proximidade_closeness(self, vertice):
        """
        Calculo da medida de proximidade de um vertice
        :param vertice: Nome do vértice
        :return:
        """
        distancias = self.dijkstra(vertice)
        soma_distancias = sum(distancias.values())
        return soma_distancias

    def identificar_pontos_criticos(self):
        """
        Indentificar os pontos criticos do grafo
        :return:
        """
        pontos_criticos = []
        maior_centralidade_interno = max(self.calcular_centralidade_grau_interno(vertice) for vertice in self.vertices)
        maior_centralidade_externo = max(self.calcular_centralidade_grau_externo(vertice) for vertice in self.vertices)
        maior_closeness = max(self.calcular_proximidade_closeness(vertice) for vertice in self.vertices)

        for vertice in self.vertices:
            if self.calcular_centralidade_grau_interno(vertice) == maior_centralidade_interno:
                pontos_criticos.append(vertice)
            elif self.calcular_centralidade_grau_externo(vertice) == maior_centralidade_externo:
                pontos_criticos.append(vertice)
            elif self.calcular_proximidade_closeness(vertice) == maior_closeness:
                pontos_criticos.append(vertice)

        return pontos_criticos

    def obter_grafo(self):
        """
        Mostra o grafo
        :return:
        """
        G = nx.Graph()
        for origem, adjacencias in self.adjacencias.items():
            for destino, peso in adjacencias:
                G.add_edge(origem, destino, weight=peso)
        return G

    def remover_vertice(self, nome):
        """
        Remove um vértice e todas as arestas adjacentes do grafo
        :param nome: Nome do vértice a ser removido
        :return:
        """
        del self.vertices[nome]
        del self.adjacencias[nome]
        for adjacencias in self.adjacencias.values():
            adjacencias = [(v, p) for v, p in adjacencias if v != nome]

    def remover_aresta(self, origem, destino):
        """
        Remove uma aresta entre dois vértices no grafo
        :param origem: Nome do vértice inicial
        :param destino: Nome do vértice de destino
        :return:
        """
        if origem in self.adjacencias and destino in self.adjacencias[origem]:
            self.adjacencias[origem] = [(v, p) for v, p in self.adjacencias[origem] if v != destino]

    def get_vertices(self):
        """
        Obtém todos os vértices do grafo
        :return:
        """
        return self.vertices.keys()

    def get_arestas(self):
        """
        Obtém todas as arestas do grafo
        :return:
        """
        arestas = []
        for origem, adjacencias in self.adjacencias.items():
            for destino, peso in adjacencias:
                arestas.append((origem, destino, peso))
        return arestas

    def bfs(self, origem):
        """
        Faz a pesquisa em largura (BFS) a partir de um vértice
        :param origem: Nome do vértice inicial
        :return:
        """
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
        """
        Faz a pesquisa em profundidade (DFS) a partir de um vértice
        :param origem: Nome do vértice inicial
        :return:
        """
        visitados = set()
        self._dfs_recursivo(origem, visitados)

    def _dfs_recursivo(self, vertice, visitados):
        """
        Faz a pesquisa em profunidade (DFS) recursivamente a partir de um vértice
        :param vertice: Nome do vértice inicial
        :param visitados: Cojunto de vértices visitados até ao momento
        :return:
        """
        visitados.add(vertice)
        print(vertice)
        for adjacente, _ in self.adjacencias[vertice]:
            if adjacente not in visitados:
                self._dfs_recursivo(adjacente, visitados)

    def dijkstra(self, origem):
        """
        Algoritmo de disjkstra para encontrar o caminho mais curto
        :param origem: Nome do vertice inicial
        :return:
        """
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
        """
        Função para interromper uma via no grafo entre dois vértices e para encontrar um/ou mais caminhos alternativos
        :param origem: O nome do vértice inicial
        :param destino: O nome do vértice de destino
        :return:
        """
        if origem in self.adjacencias and destino in self.adjacencias[origem]:
            self.remover_aresta(origem, destino)
            caminhos_alternativos = self.encontrar_caminhos_alternativos(origem, destino)
            return caminhos_alternativos
        else:
            return []

    def encontrar_caminhos_alternativos(self, origem, destino):
        """
        Função para encontrar os caminhos alternativos entre dois vértices
        :param origem: O nome do vértice de origem
        :param destino: O nome do vértice de destino
        :return:
        """
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
        """
        Função recursiva para ajudar a encontrar caminhos entre os vertices do grafo
        :param atual: O vértice atual
        :param destino: O vértice do destino
        :param caminho: O caminho percorrido até ao momento
        :param caminhos: Lista de caminhos encontrados
        :param visitados: Conjunto de vértices visitados
        :return:
        """
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

