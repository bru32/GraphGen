# Topological sorting
# Kahn's algorithm (based on in-degree)
# source:
#   ByteVigor - Topological sorting visually explained
#   https://www.youtube.com/watch?v=NX1_etRg078&list=PLZ1XikRjVdB6bMxkZOfN3Y_p02z6GiIsk
# edited by Bruce Wernick
# 19 May 2025

from collections import defaultdict, deque


def topological_sort(edges):
  """ Kahn's algorithm (based on in-degree)
      edges = list of [(u,v), ...]
      returns a node list in topological order.
  """
  graph = defaultdict(list)  # adjacency dictionary
  in_degree = defaultdict(int)

  # Build the graph and compute in-degrees
  nodes = set()
  for u, v in edges:
    graph[u].append(v)
    in_degree[v] += 1
    nodes.add(u)
    nodes.add(v)

  # Initialize queue with nodes having zero in-degree
  zero_in_degree = deque([np for np in nodes if in_degree[np] == 0])

  result = []  # node list in topological order

  while zero_in_degree:
    cp = zero_in_degree.popleft()
    result.append(cp)

    for np in graph[cp]:
      in_degree[np] -= 1
      if in_degree[np] == 0:
        zero_in_degree.append(np)

  # Check for cycles
  if len(result) != len(nodes):
    raise ValueError("Graph has at least one cycle, topological sort not possible!")

  return result


# ---------------------------------------------------------

# Example 1
#edges = [("A","C"),("B","C"),("B","D"),("C","E"),("D","F"),("E","F")] 

# Example 2 - Julie Bridge
edges = [(0,1),(0,3),(1,2),(3,2),(1,4),(2,4),(3,4)]

print(topological_sort(edges))
# The output is not unique.
# One valid result is ["A", "B", "C", "D", "E", "F"]

