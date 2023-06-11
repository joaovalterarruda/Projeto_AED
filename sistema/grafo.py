import json
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sistema.constantes import GRAFO


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
        maior_centralidade_interno = max(self.calcular_centralidade_grau_interno(vertice) for vertice in self.vertices)
        maior_centralidade_externo = max(self.calcular_centralidade_grau_externo(vertice) for vertice in self.vertices)
        maior_closeness = max(self.calcular_proximidade_closeness(vertice) for vertice in self.vertices)

        pontos_criticos = []

        for vertice in self.vertices:
            centralidade_interno = self.calcular_centralidade_grau_interno(vertice)
            centralidade_externo = self.calcular_centralidade_grau_externo(vertice)
            closeness = self.calcular_proximidade_closeness(vertice)

            if centralidade_interno == maior_centralidade_interno or centralidade_externo == maior_centralidade_externo or closeness == maior_closeness:
                pontos_criticos.append(vertice)

        return pontos_criticos

    def obter_grafo(self):
        """
        Mostra o grafo
        :return:
        """
        g = nx.DiGraph()
        for origem, adjacencias in self.adjacencias.items():
            for destino, peso in adjacencias:
                g.add_edge(origem, destino, weight=peso)
        return g

    def remover_vertice(self, nome):
        """
        Remove um vértice e todas as arestas adjacentes do grafo
        :param nome: Nome do vértice a ser removido
        :return:
        """
        if nome not in self.vertices:
            return

        del self.vertices[nome]
        del self.adjacencias[nome]

        for adjacencias in self.adjacencias.values():
            adjacencias[:] = [(v, p) for v, p in adjacencias if v != nome]

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




    def desenhar_grafo(self, nome_ficheiro_grafo, nome_ficheiro_freguesias):
        """
        Desenha o grafo a partir de um determinado ficheiro json
        :param nome_ficheiro_grafo: Nome do ficheiro json com os dados do grafo
        :param nome_ficheiro_freguesias: Nome do ficheiro json com os dados das freguesias
        :return:
        """
        with open(nome_ficheiro_grafo) as file:
            grafo_data = json.load(file)

        with open(nome_ficheiro_freguesias) as file:
            freguesias_data = json.load(file)

        g = nx.DiGraph()

        # Adicionar Freguesias ao grafo
        for freguesia in freguesias_data['freguesias']:
            g.add_node(freguesia['nome'], cor="lightgreen", tamanho=1000)

        # Adicionar vértices ao grafo
        cores = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan']
        for i, vertice in enumerate(grafo_data['vertices']):
            g.add_node(vertice['nome'], cor=cores[i % len(cores)], tamanho=200)

        # Adicionar arestas ao grafo
        for aresta in grafo_data['arestas']:
            origem = aresta['origem']
            destino = aresta['destino']
            peso = aresta['peso']
            peso_arredondado = round(peso, 2)
            g.add_edge(origem, destino, weight=peso_arredondado)

        vertices = [vertice['nome'] for vertice in grafo_data['vertices']]
        freguesias = [freguesia['nome'] for freguesia in freguesias_data['freguesias']]

        # Atualizar pos com as coordenadas dos vértices e freguesias
        pos_freguesias = {freguesia['nome']: (freguesia['longitude'], freguesia['latitude']) for freguesia in
               freguesias_data['freguesias']}
        pos_vertices = {vertice['nome']: (vertice['longitude'], vertice['latitude']) for vertice in grafo_data['vertices']}

        font_sizes_freguesia = {
            freguesia: 12 for freguesia in freguesias
        }  # Define o tamanho de fonte desejado para cada nó de freguesia

        font_sizes_vertice = {
            vertice: 0 for vertice in vertices
        }  # Define o tamanho de fonte desejado para cada nó de freguesia

        pos = {**pos_freguesias, **pos_vertices}

        plt.figure(figsize=(20, 20))

        # Desenhar nós de freguesia em primeiro plano
        node_colors_freguesia = [g.nodes[freguesia]['cor'] for freguesia in freguesias]
        node_sizes_freguesia = [g.nodes[freguesia]['tamanho'] for freguesia in freguesias]

        nx.draw_networkx_nodes(g, pos_freguesias, nodelist=freguesias,
                               node_size=node_sizes_freguesia, node_color=node_colors_freguesia)

        for node, (x, y) in pos.items(): # Ciclo para verificar como aplocar o tamanho da fonte nos rótlos dos nós
            if node in freguesias:
                font_size = font_sizes_freguesia[node]
            else:
                font_size = font_sizes_vertice[node]
            nx.draw_networkx_labels(g, {node: (x, y)}, labels={node: node}, font_size=font_size)

        # Desenhar nós de vértice em segundo plano
        node_colors_vertice = [g.nodes[vertice]['cor'] for vertice in vertices]
        node_sizes_vertice = [g.nodes[vertice]['tamanho'] for vertice in vertices]
        nx.draw_networkx_nodes(g, pos_vertices, nodelist=vertices,
                               node_size=node_sizes_vertice, node_color=node_colors_vertice, node_shape= "s")

        nx.draw_networkx_edges(g, pos_vertices, edge_color='gray', width=1, arrowsize=15, arrowstyle='->')
        edge_labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos_vertices, edge_labels=edge_labels, font_size=10)


        # Criar lista de handles para vértices e freguesias
        vertex_handles = [mpatches.Patch(color=color, label=vertice) for vertice, color in
                          zip(vertices, node_colors_vertice)]

        # Combinar as listas de handles
        all_handles = vertex_handles

        plt.legend(handles=all_handles, title='Pontos de Interesse', loc='upper right')
        plt.suptitle('Rede de Circulação: Ponta Delgada')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')

        plt.show()

    def testar_caminho(self):
        """
        Input para testar o caminho alternativo
        :return:
        """
        origem = input("Digite o nome do ponto de partida: ")
        destino = input("Digite o nome do ponto de destino: ")
        caminhos_alternativos = self.encontrar_caminhos_alternativos(origem, destino)
        if caminhos_alternativos:
            print(f"\nCaminhos alternativos entre '{origem}' e '{destino}':")
            for caminho in caminhos_alternativos:
                print(" -> ".join(caminho))

    def obter_itinerario(self):
        """
        Obter informações sobre o itinerário entre os dois pontos
        :return:
        """
        origem = input("Digite o nome do ponto de partida: ")
        destino = input("Digite o nome do ponto de destino: ")
        caminhos_alternativos = self.encontrar_caminhos_alternativos(origem, destino)
        if caminhos_alternativos:
            print(f"\nCaminhos alternativos entre '{origem}' e '{destino}':")
            for caminho in caminhos_alternativos:
                print(" -> ".join(caminho))

        distancia = self.dijkstra(origem)[destino]
        tempo_estimado_a_pe = distancia * 10  # Exemplo: 10 minutos por unidade de distância
        tempo_estimado_de_carro = distancia * 5  # Exemplo: 5 minutos por unidade de distância

        print(f"\nCaminho mais curto entre '{origem}' e '{destino}':")
        print(f"Distância a percorrer: {distancia} Km")
        print(f"Tempo estimado a pé: {tempo_estimado_a_pe} minutos")
        print(f"Tempo estimado de carro: {tempo_estimado_de_carro} minutos:)")

    def obter_arvore_rotas_carro(self, ponto_interesse, nome_ficheiro):
        """
        Obtém a subarvore de caminhos a partir de um ponto de interesse
        :param ponto_interesse: Ponto onde a árvore de caminhos de carro será obtida.
        :param nome_ficheiro: Ficheiro onde estão localizados os dados.
        :return:
        """


        # Adicionar vértices e arestas ao grafo
        with open(nome_ficheiro) as json_file:
            dados = json.load(json_file)

        for vertice in dados['vertices']:
            self.adicionar_vertice(vertice['nome'], vertice['latitude'], vertice['longitude'])

        for aresta in dados['arestas']:
            self.adicionar_aresta(aresta['origem'], aresta['destino'], aresta['peso'])

        # Obter árvore de caminhos de carro a partir do ponto de interesse
        arvore = nx.DiGraph()
        visitados = set()
        visitados.add(ponto_interesse)
        self.obter_subarvore_carro(arvore, ponto_interesse, visitados)

        # Desenhar a árvore
        self.desenhar_arvore(arvore)

    def obter_subarvore_carro(self, arvore, vertice, visitados):
        """
        Obtém a subarvore de caminhos de carro a partir de um vértice do grafo
        :param arvore: Subarvore de caminhos que está a ser construida
        :param vertice: Vértice onde a pesquisa é realizada
        :param visitados: Conjunto de vértices já visitados
        :return:
        """
        for adjacente, _ in self.adjacencias[vertice]:
            if adjacente not in visitados:
                visitados.add(adjacente)
                arvore.add_edge(vertice, adjacente)
                self.obter_subarvore_carro(arvore, adjacente, visitados)

    def desenhar_arvore(self, arvore):
        """
        Desenha um grafo que representa a árvore de um grafo
        :param arvore:
        :return:
        """
        g = nx.DiGraph()

        cores = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan']

        # Adicionar vértices ao grafo
        for i, vertice in enumerate(arvore.nodes):
            g.add_node(vertice, cor=cores[i % len(cores)])

        # Adicionar arestas ao grafo
        for origem, destino in arvore.edges:
            peso = arvore[origem][destino].get('weight', 1)  # Obtém o peso ou usa 1 como valor padrão
            peso_arredondado = round(peso, 2)
            g.add_edge(origem, destino, weight=peso_arredondado)

        pos = nx.spring_layout(g)

        plt.figure(figsize=(12, 10))
        node_colors = [g.nodes[vertice]['cor'] for vertice in g.nodes]
        nx.draw_networkx_nodes(g, pos, node_size=200, node_color=node_colors)
        nx.draw_networkx_edges(g, pos, node_size=200,
                               edge_color='gray', width=1, arrowsize=15, arrowstyle='->')
        edge_labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=8)
        nx.draw_networkx_labels(g, pos, font_size=1, font_color='black', font_weight='bold')
        handles = [mpatches.Patch(color=color, label=vertice) for vertice, color in zip(g.nodes, node_colors)]
        plt.legend(handles=handles, title='Vértices', loc='upper right')
        plt.suptitle('Rotas de percursos de carro:')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.show()

