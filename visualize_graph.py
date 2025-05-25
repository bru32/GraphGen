import networkx as nx
import matplotlib.pyplot as plt


# ---------------------------------------------------------

# Julie Bridge
graph = {
  1: [(2,200), (4,200)],
  2: [(1,200), (3,100), (5,200)],
  3: [(2,100), (4,100), (5,100)],
  4: [(1,200), (3,100), (5,200)],
  5: [(2,200), (3,100), (4,200)],
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges with weights
for node, edges in graph.items():
  for edge in edges:
    neighbor, weight = edge
    G.add_edge(node, neighbor, weight=weight)

# Draw the graph
pos = nx.spring_layout(G)  # Layout for better visualization
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=12, arrows=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Weighted Directed Graph")
plt.show()

