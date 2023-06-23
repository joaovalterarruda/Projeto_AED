from typing import Dict, List, Tuple
import heapq
import json
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import radians, sin, cos, sqrt, atan2

from TDA.Stacks.StackBasedList import StackListBased
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
        Algoritmo de Dijkstra para encontrar o caminho mais curto
        :param origem: Nome do vértice inicial
        :return: Dicionário com as distâncias mais curtas e os predecessores
        """
        distancia = {v: float('inf') for v in self.vertices}
        distancia[origem] = 0
        predecessores = {}

        fila_prioridade = [(0, origem)]

        while fila_prioridade:
            _, vertice = heapq.heappop(fila_prioridade)

            for adjacente, peso in self.adjacencias[vertice]:
                peso_total = distancia[vertice] + peso
                if peso_total < distancia[adjacente]:
                    distancia[adjacente] = peso_total
                    predecessores[adjacente] = vertice
                    heapq.heappush(fila_prioridade, (peso_total, adjacente))

        return distancia, predecessores

    # RF10
    def interromper_via(self):
        """
        Função para interromper uma via no grafo entre dois vértices e para encontrar um/ou mais caminhos alternativos
        :return: Uma lista de caminhos alternativos entre a origem e o destino no grafo modificado
        """
        arestas_disponiveis = []

        for origem, adjacencias in self.adjacencias.items():
            for adjacente, peso in adjacencias:
                arestas_disponiveis.append((origem, adjacente, peso))

        if not arestas_disponiveis:
            return []

        print("Arestas disponíveis para interromper:")
        for i, (origem, destino, peso) in enumerate(arestas_disponiveis):
            print(f"{i+1}. {origem} - {destino} (Peso: {peso})")

        opcao = int(input("Digite o número da aresta a ser removida: ")) - 1

        if opcao < 0 or opcao >= len(arestas_disponiveis):
            print("Opção inválida!")
            return []

        origem_remover, destino_remover, peso_remover = arestas_disponiveis[opcao]
        self.remover_aresta(origem_remover, destino_remover)

        origem = input("Digite o nome do vértice de origem: ")
        destino = input("Digite o nome do vértice de destino: ")

        caminhos_alternativos = self.encontrar_caminhos_alternativos(origem, destino)
        return caminhos_alternativos


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

        distancia, predecessores = self.dijkstra(origem)

        if distancia[destino] == float('inf'):
            print(f"Não existe caminho entre '{origem}' e '{destino}'")
            return

        print(f"\nCaminho mais curto entre '{origem}' e '{destino}':")
        caminho = self.reconstruir_caminho(predecessores, destino)
        print(" -> ".join(caminho))

        tempo_estimado_a_pe = distancia[destino] * 10  # Exemplo: 10 minutos por unidade de distância
        tempo_estimado_de_carro = distancia[destino] * 5  # Exemplo: 5 minutos por unidade de distância

        print(f"\nDistância a percorrer: {distancia[destino]} Km")
        print(f"Tempo estimado a pé: {tempo_estimado_a_pe} minutos")
        print(f"Tempo estimado de carro: {tempo_estimado_de_carro} minutos")

    def reconstruir_caminho(self, predecessores, destino):
        caminho = [destino]
        vertice = destino
        while vertice in predecessores:
            vertice = predecessores[vertice]
            caminho.insert(0, vertice)
        return caminho

    def obter_arvore_rotas_carro(self, ponto_interesse, nome_ficheiro, origem):
        """
        Obtém a subarvore de caminhos a partir de um ponto de interesse
        :param ponto_interesse: Ponto onde a árvore de caminhos de carro será obtida.
        :param nome_ficheiro: Ficheiro onde estão localizados os dados.
        :param origem: Nó de origem para destacar na árvore de rotas de carro.
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
        arvore = nx.Graph()
        visitados = set()
        visitados.add(ponto_interesse)
        self.obter_subarvore_carro(arvore, ponto_interesse, visitados)

        # Desenhar a árvore, destacando o nó de origem
        self.desenhar_arvore(arvore, origem)

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

    def desenhar_arvore(self, g, origem):
        """
        Desenha um grafo, destacando o nó de origem
        :param g: Grafo a ser desenhado
        :param origem: Nó de origem para destacar
        :return:
        """
        pos = nx.shell_layout(g)

        plt.figure(figsize=(12, 10))

        # Definir tamanho dos nós
        node_sizes = [200 if node != origem else 1000 for node in g.nodes]
        node_colors = ["lightblue" if node != origem else "lightgreen" for node in g.nodes]
        nx.draw(g, pos, node_color= "lightblue", edge_color='gray', width=1, arrowsize=15, arrowstyle='->')
        # Desenhar nós
        nx.draw_networkx_nodes(g, pos, node_size=node_sizes, node_color= node_colors)



        # Adicionar rótulos aos nós
        labels = {node: node for node in g.nodes}
        nx.draw_networkx_labels(g, pos, labels=labels)

        plt.suptitle('Árvore de rotas de carro')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.show()

    def shortest_path(self, origem: str, destino: str) -> List[str]:
        result = self.calculate_shortest_path(origem, destino)
        if destino not in result:
            return []  # Não há um caminho entre os vértices
        reversed_path: List[str] = []
        reversed_path.append(destino)
        current_label: str = destino
        while result[current_label][1] is not None:
            current_label = result[current_label][1]
            reversed_path.append(current_label)
        path: List[str] = reversed_path[::-1]
        return path  # Inverter a sequência do caminho para que seja do vértice de origem ao vértice de destino


    def calculate_shortest_path(self, origem: str, destino: str) -> Dict[str, Tuple[int, str]]:
        distances: Dict[str, Tuple[int, str]] = {}
        queue: List[Tuple[int, str]] = []

        if origem not in self.vertices or destino not in self.vertices:
            return distances

        distances[origem] = (0, None)
        heapq.heappush(queue, (0, origem))

        while queue:
            distance, vertex = heapq.heappop(queue)

            if vertex == destino:
                break

            if distance > distances[vertex][0]:
                continue

            for neighbor, _ in self.adjacencias[vertex]:
                new_distance = distance + self.calcular_distancia_geodesica(vertex, neighbor)

                if neighbor not in distances or new_distance < distances[neighbor][0]:
                    distances[neighbor] = (new_distance, vertex)
                    heapq.heappush(queue, (new_distance, neighbor))

        return distances

    def calcular_centralidade_grau_interno(self, vertice):
        """
        Calcula a centralidade de grau interno de um vértice no grafo
        :param vertice: O vértice para o qual se deseja calcular a centralidade de grau interno
        :return: A centralidade de grau interno do vértice
        """
        if vertice not in self.vertices:
            return 0

        return len(self.adjacencias[vertice])

    def calcular_centralidade_grau_externo(self, vertice):
        """
        Calcula a centralidade de grau externo de um vértice no grafo
        :param vertice: O vértice para o qual se deseja calcular a centralidade de grau externo
        :return: A centralidade de grau externo do vértice
        """
        if vertice not in self.vertices:
            return 0

        centralidade = 0
        for origem, adjacencias in self.adjacencias.items():
            if origem != vertice:
                for destino, _ in adjacencias:
                    if destino == vertice:
                        centralidade += 1

        return centralidade

    def calcular_closeness(self, vertice):
        """
        Calcula o closeness de um vértice no grafo com base nas distâncias geodésicas entre os vértices
        :param vertice: O vértice para o qual se deseja calcular o closeness
        :return: O closeness do vértice
        """
        if vertice not in self.vertices:
            return 0

        closeness = 0
        for v in self.vertices:
            if v != vertice:
                shortest_path = self.shortest_path(vertice, v)
                if shortest_path:
                # Utilizar a distância mais curta encontrada pelo shortest_path
                    distancia = len(shortest_path) - 1  # Subtrair 1 para excluir o vértice de origem
                    closeness += 1/distancia

        if closeness == 0:
            return 0

        closeness = (len(self.vertices)-1) / closeness
        normalized_closeness = closeness / (len(self.vertices) - 1)
        return normalized_closeness

    def calcular_distancia_geodesica(self, vertice1, vertice2):
        """
        Calcula a distância geodésica entre dois vértices do grafo com base em suas coordenadas geográficas (latitude, longitude)
        :param vertice1: O primeiro vértice
        :param vertice2: O segundo vértice
        :return: A distância geodésica em quilômetros entre os dois vértices
        """
        if vertice1 not in self.vertices or vertice2 not in self.vertices:
            return 0

        lat1, lon1 = self.vertices[vertice1]
        lat2, lon2 = self.vertices[vertice2]

        # Raio médio da Terra em quilômetros
        raio_terra = 6371.0

        # Converter graus para radianos
        lat1_rad = radians(lat1)
        lon1_rad = radians(lon1)
        lat2_rad = radians(lat2)
        lon2_rad = radians(lon2)

        # Diferença das longitudes e latitudes
        dlon = lon2_rad - lon1_rad
        dlat = lat2_rad - lat1_rad

        # Fórmula de Haversine
        a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Distância em quilômetros
        distancia = raio_terra * c
        return distancia

    def identificar_pontos_criticos(self, num_pontos=10):
        """
        Identifica os pontos críticos do grafo com base na centralidade de grau interno, grau externo e closeness
        :param num_pontos: O número de pontos críticos a serem identificados (padrão: 10)
        :return: Uma lista de tuplas contendo os vértices e as métricas de centralidade de grau interno,
                 grau externo e closeness
        """
        pontos_criticos = []
        for vertice in self.vertices:
            centralidade_grau_interno = self.calcular_centralidade_grau_interno(vertice)
            centralidade_grau_externo = self.calcular_centralidade_grau_externo(vertice)
            closeness = self.calcular_closeness(vertice)
            pontos_criticos.append((vertice, centralidade_grau_interno, centralidade_grau_externo, closeness))

        # Ordenar os pontos críticos com base na soma das métricas de centralidade
        pontos_criticos.sort(key=lambda x: sum(x[1:]), reverse=True)

        # Retornar os top n pontos críticos
        return pontos_criticos[:num_pontos]

    def mostrar_pontos_criticos(self, num_pontos=10):
        """
        Mostra os pontos críticos do grafo com base na centralidade de grau interno, grau externo e closeness
        :param num_pontos: O número de pontos críticos a serem mostrados (padrão: 10)
        """
        pontos_criticos = self.identificar_pontos_criticos(num_pontos)
        for i, (vertice, centralidade_grau_interno, centralidade_grau_externo, closeness) in enumerate(pontos_criticos, 1):
            print(f"Vértice {i}: {vertice}")
            print(f"Centralidade de Grau Interno: {centralidade_grau_interno}")
            print(f"Centralidade de Grau Externo: {centralidade_grau_externo}")
            print(f"Closeness: {closeness}")
            print()




