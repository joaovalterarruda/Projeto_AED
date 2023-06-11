import math


def calcular_distancia(lat1, lon1, lat2, lon2):
    distancia = math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)
    return distancia


# Coordenadas das freguesias
freguesias = [
    {
        "nome": "Ajuda da Bretanha",
        "latitude": 37.898056,
        "longitude": -25.756667
    },
    {
        "nome": "Arrifes",
        "latitude": 37.766667,
        "longitude": -25.7
    },
    {
        "nome": "Candelária",
        "latitude": 37.783333,
        "longitude": -25.816667
    },
    {
        "nome": "Capelas",
        "latitude": 37.833333,
        "longitude": -25.7
    },
    {
        "nome": "Covoada",
        "latitude": 37.785556,
        "longitude": -25.733056
    },
    {
        "nome": "Fajã de Baixo",
        "latitude": 37.761389,
        "longitude": -25.653889
    },
    {
        "nome": "Fajã de Cima",
        "latitude": 37.77,
        "longitude": -25.66
    },
    {
        "nome": "Fenais da Luz",
        "latitude": 37.823333,
        "longitude": -25.641389
    },
    {
        "nome": "Feteiras",
        "latitude": 37.800833,
        "longitude": -25.784167
    },
    {
        "nome": "Ginetes",
        "latitude": 37.850833,
        "longitude": -25.843889
    },
    {
        "nome": "Livramento",
        "latitude": 37.764722,
        "longitude": -25.603611
    },
    {
        "nome": "Mosteiros",
        "latitude": 37.893056,
        "longitude": -25.816944
    },
    {
        "nome": "Pilar da Bretanha",
        "latitude": 37.905278,
        "longitude": -25.781111
    },
    {
        "nome": "Relva",
        "latitude": 37.754722,
        "longitude": -25.720556
    },
    {
        "nome": "Remédios",
        "latitude": 37.886111,
        "longitude": -25.736111
    },
    {
        "nome": "Santa Bárbara",
        "latitude": 37.875,
        "longitude": -25.726389
    },
    {
        "nome": "Santa Clara",
        "latitude": 37.734444,
        "longitude": -25.683333
    },
    {
        "nome": "Santo António",
        "latitude": 37.854444,
        "longitude": -25.703056
    },
    {
        "nome": "São José",
        "latitude": 37.7386,
        "longitude": -25.6768
    },
    {
        "nome": "São Pedro",
        "latitude": 37.740556,
        "longitude": -25.663611
    },
    {
        "nome": "São Roque",
        "latitude": 37.748889,
        "longitude": -25.633333
    },
    {
        "nome": "São Sebastião",
        "latitude": 37.742222,
        "longitude": -25.675
    },
    {
        "nome": "São Vicente Ferreira",
        "latitude": 37.818333,
        "longitude": -25.665833
    },
    {
        "nome": "Sete Cidades",
        "latitude": 37.858889,
        "longitude": -25.794444
    }
]

# Criar o grafo com as arestas e pesos
grafo = {}

for i in range(len(freguesias)):
    freguesia1 = freguesias[i]
    nome1 = freguesia1["nome"]
    latitude1 = freguesia1["latitude"]
    longitude1 = freguesia1["longitude"]
    arestas = {}

    for j in range(i + 1, len(freguesias)):
        freguesia2 = freguesias[j]
        nome2 = freguesia2["nome"]
        latitude2 = freguesia2["latitude"]
        longitude2 = freguesia2["longitude"]

        distancia = calcular_distancia(latitude1, longitude1, latitude2, longitude2)*100
        arestas[nome2] = distancia
        # Se o grafo for não direcionado, adicionar também a aresta inversa
        # arestas[nome1] = distancia

    grafo[nome1] = arestas

# Exibir o grafo com as arestas e pesos
for vertice, arestas in grafo.items():
    print(f"{vertice}: {arestas}")
