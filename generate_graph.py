# Generate Random Graph
#   Random geometric graph (RGG)
#   k-Nearest Neighbor Graph (k-NNG)
#
# based on:
#   Pathfinding Algorithms in C# by KristianEkman
#   https://www.codeproject.com/Articles/1221034/Pathfinding-Algorithms-in-Csharp
#
# translated to Python (and heavily edited):
# Bruce Wernick
# 20 May 2025

import math
from collections import defaultdict
from random import random as rnd  # shortcut to random float point number
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


# ---------------------------------------------------------

class Node:

  Count = 0  # node counter class variable used to assign new node id's

  def __init__(self):
    """ Constructor returns a new Node,
        position at random (x,y)
    """
    
    # use latest Count as the node identifier
    self.id = Node.Count
    Node.Count += 1
    
    self.edgelinks = []  # links to outgoing connected edges
    
    # random (x,y) position on creation
    self.x = round(rnd(), 4)
    self.y = round(rnd(), 4)

  def dist(self, other):
    """ Return distance between self and other node
    """
    return math.dist((self.x, self.y), (other.x, other.y))

  def too_close_to_any(self, others):
    """ Test if self is too close to any others.
        The scale is 0..1 so tol=0.02 means a 2% tolerance.
    """
    tol = 0.02
    return any(self.dist(other) < tol for other in others)

  def connect_closest_nodes(self, nodes, link_count):
    """ Connect self to closest link_count nodes
    """
    
    # Sort by distance from self to all other nodes to create a candidate list
    # Create a new list of edges (sorted by distance from all nodes)
    candidates = sorted((Edge(np, self.dist(np)) for np in nodes if np.id != self.id), key=lambda x: x.length)
    
    # add link_count number of candidates
    acc = 0  # accumulator
    for ep in candidates:
      if acc >= link_count:
        break
        
      # make sure candidate (ep) is not already connected
      if not any(cp.othernode == ep.othernode for cp in self.edgelinks):
        self.edgelinks.append(ep)
        acc += 1
        
        if not any(cp.othernode == self for cp in ep.othernode.edgelinks):
          
          # Create a new edge and add it to othernode edgelinks
          newEdge = Edge(self, ep.length)
          ep.othernode.edgelinks.append(newEdge)


# ---------------------------------------------------------

class Edge:

  def __init__(self, othernode, length):
    """ Construct new edge to othernode
    """
    self.othernode = othernode  # link to other connected node
    self.length = length
    

# ---------------------------------------------------------

class Graph:
  
  def __init__(self, node_count, link_count):
    """ Construct new random graph.
    """

    # Create empty nodes list
    self.nodes = []

    # Populate with nodes (ensuring separation).
    while len(self.nodes) < node_count:
      np = Node()
      if not np.too_close_to_any(self.nodes):
        self.nodes.append(np)

    # Connect nodes with link_count closest nodes.    
    for np in self.nodes:
      np.connect_closest_nodes(self.nodes, link_count)


# ---------------------------------------------------------

def plot_graph(graph):
  """ Plot graph using matplotlib.
  """
  fig, ax = plt.subplots(figsize=(9, 5))

  # plot edges
  lines = [[(np.x, np.y), (ep.othernode.x, ep.othernode.y)] for np in graph.nodes for ep in np.edgelinks]
  ax.add_collection(LineCollection(lines, colors='lightgray', alpha=0.25, linewidths=1))
  
  # plot nodes
  X = [node.x for node in graph.nodes]
  Y = [node.y for node in graph.nodes]
  ax.scatter(X, Y, c='blue', s=15)
  
  ax.set(xlim=(-0.1, 1.1), ylim=(-0.1, 1.1), title="Random Geometric Graph (RGG)")
  plt.grid(False)
  plt.show()

# ---------------------------------------------------------

def generate_adj(graph):
  """ Generate adjacency dictionary from graph. 
  """
  adj = {}
  for node in graph.nodes:
    edgelist = []
    for ep in node.edgelinks:
      edgelist.append((ep.othernode.id, round(ep.length, 4)))
    adj[node.id] = edgelist
  return adj


# ---------------------------------------------------------

if __name__ == "__main__":
  
  graph = Graph(node_count=100, link_count=3)
  
  #print("Nodes:")
  #for node in graph.nodes:  
  #  print(f"{node.id}: x={node.x}, y={node.y}")
  #print()

  # Create node list
  #node_list = []
  #for node in graph.nodes:  
  #  node_list.append((node.x, node.y))
  #print(node_list)
  #print(len(node_list))

  # Generate the adjacency dictionary.
  #adj = generate_adj(graph)
  #print("Adjacency Dictionary:")
  #for (node, edges) in adj.items():
  #  print(f"{node}: {edges}")
  #print()

  # Generate edges list.
  #edges = set()
  #for np in graph.nodes:
  #  for ep in np.edgelinks:
  #    u, v = np.id, ep.othernode.id
  #    if u < v:
  #      edges.add((u, v, round(ep.length, 4)))
  #print("Edges:")
  #for ep in sorted(edges):
  #  print(f"{ep}")
  #print(f"{len(edges)} edges in list.")

  # Compact way to build the edge list. 
  #lines = sorted([(a.id, b.othernode.id) for a in graph.nodes for b in a.edgelinks if a.id < b.othernode.id])
  #for line in lines:
  #  print(line)   
  #print(len(lines))

  plot_graph(graph)
