import networkx as nx
import matplotlib.pyplot as plt

# Criando o grafo
G = nx.DiGraph()

# Adicionando os vértices
vertices = [
    {"nome": "Praia das Milicias", "latitude": 37.750964, "longitude": -25.623417000000018},
    {"nome": "Praia do Pópulo", "latitude": 37.7503986, "longitude": -25.618265399999927},
    {"nome": "Portas do Mar", "latitude": 37.73935282483711, "longitude": -25.662707267150836},
    {"nome": "Vista do Rei", "latitude": 37.839233, "longitude": -25.794891300000018},
    {"nome": "Lagoa das Sete Cidades", "latitude": 37.86128473395813, "longitude": -25.79628476415881},
    {"nome": "Ponta da Ferraria", "latitude": 37.86082765045781, "longitude": -25.852460861206055},
    {"nome": "Universidade dos Açores", "latitude": 37.74588065027564, "longitude": -25.663613965021664},
    {"nome": "Igreja da Matriz", "latitude": 37.7399875, "longitude": -25.668544200000042},
    {"nome": "Ermida da Mãe de Deus", "latitude": 37.743817220597066, "longitude": -25.660897493362427}
]

for i, vertice in enumerate(vertices, start=1):
    G.add_node(i, **vertice)

# Adicionando as arestas
arestas = [
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 8),
    (8, 9),
    (9, 1)
]

G.add_edges_from(arestas)

# Visualizando o grafo
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, edge_color="gray", arrows=True)
plt.title("Grafo de Rede de Circulação")
plt.axis("off")
plt.show()
