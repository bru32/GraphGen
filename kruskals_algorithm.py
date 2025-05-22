# Minimum Spanning Tree by Kruskal's Algorithm
# ByteVigor - Kruskal’s Algorithm Visually Explained (Minimum Spanning Tree)
# https://www.youtube.com/watch?v=OxfTT8slSLs&list=PLZ1XikRjVdB6bMxkZOfN3Y_p02z6GiIsk&index=3
# Edited by Bruce Wernick
# 19 May 2024


class UnionFind:
  def __init__(self, n):
    self.parent = list(range(n))
    self.rank = [0]*n  # for union by rank

  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])  # Path compression
    return self.parent[x]

  def union(self, x, y):
    x0 = self.find(x)
    y0 = self.find(y)
    if x0 == y0:
      return False
    if self.rank[x0] < self.rank[y0]:
      self.parent[x0] = y0
    elif self.rank[x0] > self.rank[y0]:
      self.parent[y0] = x0
    else:
      self.parent[y0] = x0
      self.rank[x0] += 1
    return True

def kruskal(indexed_edges, num_nodes):
  """ Kruskal's algorithm implemented for indexed nodes.
  """
  uf = UnionFind(num_nodes)
  indexed_edges.sort()
  mst = []
  weight = 0  # total
  for w,u,v in indexed_edges:
    if uf.union(u, v):
      mst.append((u,v,w))
      weight += w
    if len(mst) == num_nodes - 1:
      break
  return mst, weight

def prepare_indexed_edges(edges):
  """ Input a list of edges (weight, u, v)
      output indexed edges, number of nodes and string to index mapping.
  """
  nodes = set()
  for _,u,v in edges:
    nodes.update([u,v])

  node_to_index = {node: idx for idx, node in enumerate(sorted(nodes))}
  index_to_node = {idx: node for node, idx in node_to_index.items()}
  indexed_edges = [(w, node_to_index[u], node_to_index[v]) for w, u, v in edges]

  return indexed_edges, len(nodes), node_to_index, index_to_node


def restore_mst_labels(mst_indexed, index_to_node) :
  """ Convert MST from indexed form to labelled form.
  """
  return [(index_to_node[u], index_to_node[v], w) for u, v, w in mst_indexed]


# ---------------------------------------------------------

# Example
edges = [
  (7, "A", "B"),
  (1, "A", "C"),
  (5, "B", "C"),
  (6, "B", "D"),
  (3, "C", "D"),
  (4, "C", "E"),
  (2, "D", "E"),
]

indexed_edges, num_nodes, node_to_index, index_to_node = prepare_indexed_edges(edges)
mst_indexed, total = kruskal(indexed_edges, num_nodes)
mst_labeled = restore_mst_labels(mst_indexed, index_to_node)

for u, v, w in mst_labeled:
  print(f"{u} - {v} (weight: {w})")
print(mst_labeled)
print(f"Total weight: {total}")

