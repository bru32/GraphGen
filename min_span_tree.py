# Minimum spanning tree

from collections import defaultdict


class Graph:
  
  def __init__(self):
    self.edges = []
    self.adj = defaultdict(dict)
  
  def add_edge(self, u, v, weight):

    # Ensure consistent order
    if v < u:  
      u, v = v, u

    # Avoid duplicates
    if (u, v) not in [(x, y) for (w, x, y) in self.edges]:
      self.edges.append((weight, u, v))
    
    # Update adjacency dictionary
    self.adj[u][v] = weight
    self.adj[v][u] = weight

  def get_edges_sorted(self):
    return sorted(self.edges)  # (weight, u, v)

  def get_adj(self):
    return self.adj


# ---------------------------------------------------------

def kruskal(graph):
  """ Return minimum spanning tree by Kruskal's method.
  """
  edges = graph.get_edges_sorted()
  nodes = set()
  
  # Collect all unique nodes
  for weight, u, v in edges:
    nodes.add(u)
    nodes.add(v)
  
  # Union-Find data structure
  parent = {node: node for node in nodes}
  rank = {node: 0 for node in nodes}

  def find(u):
    while parent[u] != u:
      parent[u] = parent[parent[u]]  # Path compression
      u = parent[u]
    return u

  mst = []
  for weight, u, v in edges:
    ru = find(u)
    rv = find(v)
    if ru != rv:
      mst.append((u, v, weight))
      
      # Union by rank
      if rank[ru] > rank[rv]:
        parent[rv] = ru
      else:
        parent[ru] = rv
        if rank[ru] == rank[rv]:
          rank[rv] += 1
  return mst


# ---------------------------------------------------------

# Example usage
graph = Graph()

graph.add_edge(0, 1, 300)
graph.add_edge(0, 3, 320)
graph.add_edge(1, 2, 100)
graph.add_edge(1, 4, 300)
graph.add_edge(2, 3, 150)
graph.add_edge(2, 4, 200)
graph.add_edge(3, 4, 100)

mst = kruskal(graph)
for u, v, weight in mst:
  print(f"{u}, {v}, {weight}")

