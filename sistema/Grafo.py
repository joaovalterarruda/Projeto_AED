class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = {}
        self.coordenadas = {}

    # Métodos de adição e remoção de vértices
    def adicionar_vertice(self, vertice, coordenadas):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}
            self.coordenadas[vertice] = coordenadas

    def remover_vertice(self, vertice):
        if vertice in self.vertices:
            del self.vertices[vertice]
            del self.coordenadas[vertice]
            # Remove as arestas que estão conectadas ao vértice
            for v in self.vertices:
                if vertice in self.vertices[v]:
                    del self.vertices[v][vertice]

    # Métodos de adição e remoção de arestas
    def adicionar_aresta(self, origem, destino, distancia, velocidade_min, velocidade_max, tempo_pe, tempo_carro):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem][destino] = {
                'distancia': distancia,
                'velocidade_min': velocidade_min,
                'velocidade_max': velocidade_max,
                'tempo_pe': tempo_pe,
                'tempo_carro': tempo_carro
            }
            # Cria uma entrada reversa para permitir movimento bidirecional (opcional)
            self.vertices[destino][origem] = {
                'distancia': distancia,
                'velocidade_min': velocidade_min,
                'velocidade_max': velocidade_max,
                'tempo_pe': tempo_pe,
                'tempo_carro': tempo_carro
            }
            # Mantém um registro das arestas
            self.arestas[(origem, destino)] = {
                'distancia': distancia,
                'velocidade_min': velocidade_min,
                'velocidade_max': velocidade_max,
                'tempo_pe': tempo_pe,
                'tempo_carro': tempo_carro
            }

    def remover_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices[origem]:
            del self.vertices[origem][destino]
            # Remove a entrada reversa correspondente (opcional)
            del self.vertices[destino][origem]
            # Remove o registro da aresta
            del self.arestas[(origem, destino)]

    # Métodos de consulta de vértices e arestas
    def consultar_vertice(self, vertice):
        if vertice in self.vertices:
            return self.vertices[vertice]

    def consultar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices[origem]:
            return self.vertices[origem][destino]

    def consultar_coordenadas(self, vertice):
        if vertice in self.coordenadas:
            return self.coordenadas[vertice]

    def consultar_todos_vertices(self):
        return self.vertices.keys()

    def consultar_todas_arestas(self):
        return self.arestas.keys()
