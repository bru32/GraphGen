# Generate RGG
# https://en.wikipedia.org/wiki/Random_geometric_graph
# Bruce Wernick
# 21 May 2025

import random
import math
from collections import namedtuple
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# ---------------------------------------------------------

Point = namedtuple("Point", ["x", "y"])

def rnd():
  return round(random.random(), 4)

# ---------------------------------------------------------

def generate_RGG(n=200, rad=0.15):
  """ Generate RGG
      Returns:
        node list [(x,y), ...]  x and y are coords
        edge list [(u,v), ...]  u and v are node indices
  """
  nodes = []
  for _ in range(n):
    cp = Point(rnd(), rnd())
    nodes.append(cp)
  edges = []
  for i in range(n):
    a = nodes[i]
    for j in range(i+1, n):
      b = nodes[j]
      dist = math.dist((a.x, a.y), (b.x, b.y))
      if dist <= rad:
        edges.append((i, j))
  return nodes, edges

def plot_graph(nodes, edges):
  """ Plot graph with matplotlib
  """
  fig, ax = plt.subplots(figsize=(9, 5))

  # plot edges
  lines = []
  for ep in edges:
    x1, y1 = nodes[ep[0]]
    x2, y2 = nodes[ep[1]]
    lines.append([(x1, y1), (x2, y2)]) 
  ax.add_collection(LineCollection(lines, colors='gray', alpha=0.25, linewidths=1))
  
  # plot nodes
  x, y = zip(*nodes)
  ax.scatter(x, y, c='blue', s=15)
  
  ax.set(xlim=(-0.1, 1.1), ylim=(-0.1, 1.1), title="Random Geometric Graph (RGG)")
  plt.grid(False)
  plt.show()

# ---------------------------------------------------------

nodes, edges = generate_RGG(200)
#print("nodes: ", nodes)
#print("edges: ", edges)
plot_graph(nodes, edges)
