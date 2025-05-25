# Graph Node Coloring

def greedy_coloring(graph):
  result = {}
  colors = set()
  for cp in graph:
    colors = set(range(len(graph)+1))
    for np in graph[cp]:
      if np in result:
        colors.discard(result[np])
    if colors:
      result[cp] = min(colors)
    else:
      result[cp] = len(graph)
  return result


# ---------------------------------------------------------

graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D', 'E'],
  'C': ['A', 'F'],
  'D': ['B'],
  'E': ['B', 'F'],
  'F': ['C', 'E']}


graph_color = greedy_coloring(graph)
print(graph_color)
