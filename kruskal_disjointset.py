# Kruskal with disjointSet

class DisjointSet:
  def __init__(self, nodes):
    self.parent = {np: np for np in nodes}
    self.rank = {np: 0 for np in nodes}

  def find(self, node):
    if self.parent[node] != node:
      self.parent[node] = self.find(self.parent[node])
    return self.parent[node]

  def union(self, r1, r2):
    if self.rank[r1] > self.rank[r2]:
      self.parent[r2] = r1
    elif self.rank[r1] < self.rank[r2]:
      self.parent[r1] = r2
    else:
      self.parent[r2] = r1
      self.rank[r1] += 1

def kruskal(graph):
  """ Return Min Spanning Tree (list) of graph.
      graph is an adjacency list.
  """
  edges = []
  for cp, neighbors in graph.items():
    for np, weight in neighbors:
      if (np, cp, weight) not in edges:
        edges.append((cp, np, weight))
  edges.sort(key=lambda edge: (edge[2], edge[0], edge[1]))
  disjoint_set = DisjointSet(graph.keys())
  mst = []
  for u, v, weight in edges:
    ru = disjoint_set.find(u)
    rv = disjoint_set.find(v)
    if ru != rv:
      mst.append((u, v, weight))
      disjoint_set.union(ru, rv)
  return mst


# ---------------------------------------------------------

# Julie Bridge
graph = {
  1: [(2,200), (4,200)],
  2: [(3,700), (5,200)],
  3: [(5,100)],
  4: [(3,100), (5,200)],
  5: [(1,500)]}

mst = kruskal(graph)
print(mst)
