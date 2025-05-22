# Water flow network using the Hardy Cross method.
# Bruce Wernick
# 14 May 2025

from collections import defaultdict

class Graph():

  def __init__(self):
    self.edges = set()
    self.nodes = set()
    self.adj = defaultdict(set)

  def report(self):
    #print(self.nodes)
    #print(self.edges)
    print(self.adj)

  def addEdge(self, a, b, c):
    self.nodes.add(a)
    self.nodes.add(b)
    self.edges.add(c)
    self.adj[a].add(b)
    self.adj[b].add(a)

  def has_key(self, cp):
    return cp in self.adj

  def neighbors(self, a):
    return self.adj[a]


# ---------------------------------------------------------

def find_path(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return path
  if not graph.has_key(start):
    return None
  for node in graph.neighbors(start):
    if node not in path:
      newpath = find_path(graph, node, end, path)
      if newpath:
        return newpath
  return None

# ---------------------------------------------------------

graph = Graph()
graph.addEdge(1, 2, 1)
graph.addEdge(1, 4, 2)
graph.addEdge(2, 3, 3)
graph.addEdge(4, 3, 4)
graph.addEdge(2, 5, 5)
graph.addEdge(3, 5, 6)
graph.addEdge(4, 5, 7)
graph.addEdge(5, 1, 8)

path = find_path(graph, 1, 5)
print("path=", path)

