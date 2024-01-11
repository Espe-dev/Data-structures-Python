import networkx as nx
from time import time
start = time()
# Création d'un graphe pondéré
G = nx.Graph()
G.add_edge('A', 'B', weight=3)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=5)
G.add_edge('B', 'D', weight=1)
G.add_edge('C', 'D', weight=2)

# Application de l'algorithme de Dijkstra pour trouver le chemin le plus court
shortest_path = nx.shortest_path(G, source='A', target='D', weight='weight')
print(f"Temps d'éxecution dudit algorithme : {time() - start} secondes")
print("Chemin le plus court :", shortest_path)