import json
import math

def calcular_distancia(lat1, lon1, lat2, lon2):
    R = 6371  # Raio médio da Terra em km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = R * c
    return distancia

# Carregar dados do arquivo JSON
with open('pontos_interesse.json', 'r') as arquivo:
    dados_json = json.load(arquivo)

# Criar uma lista de dicionários para os vértices
vertices = []
for ponto in dados_json:
    vertices.append({"nome": ponto['designacao'], 'latitude': ponto['latitude'], 'longitude': ponto['longitude']})

# Calcular as distâncias entre os pontos e criar as arestas
arestas = []
for i in range(len(dados_json) - 1):
    ponto1 = dados_json[i]
    ponto2 = dados_json[i + 1]
    distancia = calcular_distancia(ponto1['latitude'], ponto1['longitude'], ponto2['latitude'], ponto2['longitude'])
    origem = ponto1['designacao']
    destino = ponto2['designacao']
    arestas.append({"origem": origem, "destino": destino, "peso": distancia})
    arestas.append({"origem": destino, "destino": origem, "peso": distancia})

    if i + 2 < len(dados_json):
        ponto3 = dados_json[i + 2]
        distancia2 = calcular_distancia(ponto1['latitude'], ponto1['longitude'], ponto3['latitude'], ponto3['longitude'])
        destino2 = ponto3['designacao']
        arestas.append({"origem": origem, "destino": destino2, "peso": distancia2})
        arestas.append({"origem": destino2, "destino": origem, "peso": distancia2})

        distancia3 = calcular_distancia(ponto2['latitude'], ponto2['longitude'], ponto3['latitude'], ponto3['longitude'])
        arestas.append({"origem": destino, "destino": destino2, "peso": distancia3})
        arestas.append({"origem": destino2, "destino": destino, "peso": distancia3})

# Estrutura final do grafo
grafo = {'vertices': vertices, 'arestas': arestas}

# Gravar o resultado em um arquivo JSON
with open('../main/grafo.json', 'w') as arquivo:
    json.dump(grafo, arquivo, indent=4)

print("Grafo gravado em grafo.json.")
