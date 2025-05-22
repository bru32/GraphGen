# Bellman-Ford graph search algorithm
# source: 
#   ByteVigor - Bellman-Ford Shortest Path Algorithm Visually Explained
#   https://www.youtube.com/watch?v=Mn9bFIIyXIM
# Updated by Bruce Wernick
# 19 May 2025

import math


def trace_path(came_from, start, goal):
  """ Retrace came_from dictionary to get the shortest path 
      from start to goal.
  """
  if came_from[goal] is None:
    return f"No path found from {start} to {end}"
  path = []
  cp = goal
  while cp is not None:
    path.append(cp)
    cp = came_from[cp]
  return list(reversed(path))

def bellman_ford(edges, start, nodes):
  """ Bellman-Ford graph search for shortest path.
      Allows for negative weights
      edges = edge list [(u,v,weight), ... ]
      start = node name
      nodes = node list ['A', ... ]
  """
  
  # Initialize distances and came_from
  distances = {node: math.inf for node in nodes}
  distances[start] = 0
  came_from = {node: None for node in nodes}
  iteration_results = []

  # Relaxation for n-1 iterations
  for _ in range(len(nodes)-1):
    updated = False  # Record if there is an update

    for u, v, weight in edges:
      if distances[u] != math.inf and distances[u] + weight < distances[v]:
        distances[v] = distances[u] + weight
        came_from[v] = u  # Record predecessor
        updated = True

    iteration_results.append(distances.copy())  # Record each round result

    # If no updates in this round, stop early
    if not updated:
      break

  # Detect negative weight cycle
  for u, v, weight in edges:
    if distances[u] != math.inf and distances[u] + weight < distances[v]:
      return f"There is a negative weight cycle in the graph."

  return distances, came_from, iteration_results


# ---------------------------------------------------------

# Define the edges and nodes
edges = [
  ("A", "B", 6),
  ("A", "C", 4),
  ("A", "D", 5),
  ("B", "E", -1),
  ("C", "B", -2),
  ("C", "E", 3),
  ("D", "C", -2),
  ("D", "F", -1),
  ("E", "F", 3),
]

# Create nodes list
nodes = list(sorted({node for edge in edges for node in edge[:2]}))
#print(f"Nodes: {nodes}")

start = "A"
result = bellman_ford(edges, start, nodes)

# Output result
if isinstance(result, str):  # Negative weight cycle case
  print(result)
else:
  final_distances, came_from, iteration_results = result
  #print(f"iteration_results")
  #for item in iteration_results:
  #  print(f"{item}")
  print(f"final_distances = {final_distances}")
  goal = "F"
  path = trace_path(came_from, start, goal)
  dist = final_distances[goal]
  print(f"Path {start} to {goal} = {path}, dist = {dist}")
  