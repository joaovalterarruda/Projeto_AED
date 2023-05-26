import json
import matplotlib.pyplot as plt
from graph import Graph


# Create an instance of the Graph class
graph = Graph()

# Load data from the JSON file
with open("pontos_interesse.json", 'r') as file:
    data = json.load(file)

# Add vertices to the graph
for ponto in data:
    designacao = ponto['designacao']
    latitude = ponto['latitude']
    longitude = ponto['longitude']
    graph.add_vertex(designacao, {'latitude': latitude, 'longitude': longitude})

# Visualize the graph
graph.map_network()

# Show the plot
plt.show()
