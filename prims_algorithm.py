# Minimum Spanning Tree by Prim's Algorithm.
# Source:
#   ByteVigor: Prim's Algorithm Visually Explained (Minimum Spanning Tree)
#   https://www.youtube.com/watch?v=20QfaLQPLqQ&list=PLZ1XikRjVdB6bMxkZOfN3Y_p02z6GiIsk&index=2
# Edited by Bruce Wernick
# 19 May 2025 

import heapq
from collections import defaultdict


class PriorityQueue:
  def __init__(self):
    self.items = []
  def push(self, u, v, priority):
    heapq.heappush(self.items, (priority, u, v))
  def pop(self):
    priority, u, v = heapq.heappop(self.items)
    return (u, v, priority)
  def __call__(self):
    return len(self.items) > 0

def prim(edges):
  """ Minimum Spanning Tree by Prim's Algorithm.
      edges = list of [(u, v, weight), ... ]
      returns 
        list containing the minimum spanning tree.
        and total weight.
  """
  
  # Build adjacency list and nodes set
  graph = defaultdict(list)
  nodes = set()
  for u, v, w in edges:
    graph[u].append((v,w))
    graph[v].append((u,w))
    nodes.update([u,v])
  n = len(nodes)

  seen = set()
  mst = []  # initialize min spanning tree
  weight = 0  # total weight
  pq = PriorityQueue()

  u = edges[0][0]  # Choose any starting point
  seen.add(u)
  for (v, w) in graph[u]:
    pq.push(u, v, w)

  while pq() and len(mst) < n-1:
    (u, v, w) = pq.pop()
    if v not in seen:
      seen.add(v)
      mst.append((u, v, w))
      weight += w
      for (np, w2) in graph[v]:
        if np not in seen:
          pq.push(v, np, w2)

  return mst, weight


# ---------------------------------------------------------

# Example 1
edges = [("A", "B", 2), ("A", "C", 3),
  ("B", "C", 1), ("B", "D", 4),
  ("C", "D", 5), ("C", "E", 6),
  ("D", "E", 2), ("D", "F", 3),
  ("E", "F", 4)]

# Example 2: Julie Bridge
edges = [(0,1,600),(0,3,500),(1,2,200),(3,2,200),(1,4,500),(2,4,200),(3,4,500),(4,0,999)]

mst, weight = prim(edges)
print(f"{mst=}")
print(f"{weight=}")
print()
