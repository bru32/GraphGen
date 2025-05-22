# Given an edge list, find the basic circuits (based on cost).
# Bruce Wernick
# 16 May 2025

import heapq
from collections import deque, defaultdict

class Graph:
  """ Graph data class.
  """
  def __init__(self):
    """Construct new Graph class"""
    self.edges = None
    self.adj = None

  def cost(self, cp, np):
    """ Return the cost of edge (cp, np)
    """
    for node in self.adj[cp]:
      if node[0] == np:
        return node[1]["cost"]
    return 1

  def neighbors(self, id):
    """ Return a list of nodes adjacent to id
    """
    return [item[0] for item in self.adj[id]]

  def cost_neighbors(self, id):
    """ Return list of (v, edge_dict)
    """
    return self.adj[id]

class PriorityQueue:
  """ Priority Queue class.
  """
  def __init__(self):
    self.elements = []
  
  def empty(self):
    return not self.elements
  
  def put(self, item, priority):
    heapq.heappush(self.elements, (priority, item))

  def get(self):
    return heapq.heappop(self.elements)[1]

def retrace(came_from, start, goal):
  """ Reconstruct path using came_from dictionary.
  """
  cp = goal
  path = []
  if goal not in came_from:
    return []
  while cp != start:
    path.append(cp)
    cp = came_from[cp]
  path.append(start)
  path.reverse()
  return path

def search(graph, start, goal):
  """ dfs through graph from start to goal.
  """
  que = PriorityQueue()
  que.put(start, 0)
  came_from = {}
  cost_so_far = {}
  came_from[start] = None
  cost_so_far[start] = 0
  while not que.empty():
    cp = que.get()
    if cp == goal:
      break
    for np in graph.neighbors(cp):
      new_cost = cost_so_far[cp] + graph.cost(cp, np)
      if np not in cost_so_far or new_cost < cost_so_far[np]:
        cost_so_far[np] = new_cost
        priority = new_cost
        que.put(np, priority)
        came_from[np] = cp
  return retrace(came_from, start, goal)

class UnionFind:
  """ Union find algorithm.
  """
  def __init__(self, size):
    self.parent = list(range(size))
    self.rank = [0] * size
  
  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]
  
  def union(self, x, y):
    x0 = self.find(x)
    y0 = self.find(y)
    
    if x0 == y0:
      return False  # Already in the same set
    
    if self.rank[x0] < self.rank[y0]:
      self.parent[x0] = y0
    else:
      self.parent[y0] = x0
    
    if self.rank[x0] == self.rank[y0]:
      self.rank[x0] += 1
    
    return True

def kruskal_mst(edges, num_nodes):
  """ Minimum spanning treee by Kruskal's method.
  """
  edges.sort(key=lambda x: x[2]["cost"])  # Sort edges by cost
  uf = UnionFind(num_nodes)
  mst = []
  for u, v, edge_dict in edges:
    if uf.union(u, v):
      mst.append((u, v, edge_dict))
  return mst

def prim_mst(graph, start_node=0):
  """ Minimum spanning treee by Prim's method.
  """
  mst = []
  visited = set([start_node])
  edges = [(edge_dict["cost"], start_node, to) for to, edge_dict in graph.adj[start_node]]
  heapq.heapify(edges)
  while edges:
    cost, u, v = heapq.heappop(edges)
    if v not in visited:
      visited.add(v)
      mst.append((u, v, {"cost": cost}))
      for np, edge_dict in graph.cost_neighbors(v):
        if np not in visited:
          heapq.heappush(edges, (edge_dict["cost"], v, np))
  return mst

def to_adj(edges):
  """ Convert edge list [(u, v, {"cost":c})...] to adjacency dictionary.
  """
  adj = defaultdict(list)
  for (u, v, edge_dict) in edges:
    adj[u].append((v, edge_dict))
    adj[v].append((u, edge_dict))
  return adj

# ---------------------------------------------------------

graph = Graph()

# Example (Julie Bridge)
#      0 ────┐
#    ╱   ╲   │
#   1──2──3  │
#    ╲ | ╱   │
#      4 ────┘

# Define graph by costed edge list.
# [(from, to, {"cost": value}) ... ]
graph.edges = [
  (0, 1, {"id": 1, "cost": 100, "flow": 0, "id": 80, "length": 100}),
  (0, 3, {"id": 2, "cost": 900, "flow": 0, "id": 80, "length": 900}),
  (1, 2, {"id": 3, "cost": 100, "flow": 0, "id": 80, "length": 100}),
  (3, 2, {"id": 4, "cost": 100, "flow": 0, "id": 80, "length": 100}),
  (1, 4, {"id": 5, "cost": 900, "flow": 0, "id": 80, "length": 900}),
  (2, 4, {"id": 6, "cost": 900, "flow": 0, "id": 80, "length": 900}),
  (3, 4, {"id": 7, "cost": 100, "flow": 0, "id": 80, "length": 100}),
  (4, 0, {"id": 8, "cost": 999, "flow": 0, "id": 80, "length": 999})]

graph.adj = to_adj(graph.edges)

start, goal = 0, 4
path = search(graph, start, goal)
print(path)

# Try two diferent methods to find the MST
num_nodes = len(graph.adj)
mst = kruskal_mst(graph.edges, num_nodes)
print(f"mst: {mst}")
mst = prim_mst(graph, 0)
print(f"mst: {mst}")

# Remove the mst from the edge list to reveal the basic edges.
basic = []
for e in graph.edges:
  u, v, edge_dict = e
  if (u, v, edge_dict) not in mst and (v, u, edge_dict) not in mst:
    basic.append(e)
print(f"basic: {basic}")

# Find Basic Circuits
g = Graph()
adj = to_adj(mst)
g.adj = adj
for i, (u, v, edge_dict) in enumerate(basic):
  path = search(g, v, u)
  print(f"circ[{i}]: {path}")

