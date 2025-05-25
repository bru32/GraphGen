# Testing Prim's Algorithm


class Graph:
  def __init__(self, size):
    self.adj_matrix = [[0] * size for _ in range(size)]
    self.size = size
    self.vertex_data = [''] * size

  def add_edge(self, u, v, weight):
    if 0 <= u < self.size and 0 <= v < self.size:
      self.adj_matrix[u][v] = weight
      self.adj_matrix[v][u] = weight  # For undirected graph

  def add_vertex_data(self, vertex, data):
    if 0 <= vertex < self.size:
      self.vertex_data[vertex] = data

  def prims_algorithm(self):
    in_mst = [False] * self.size
    key_values = [float('inf')] * self.size
    parents = [-1] * self.size

    key_values[0] = 0  # Starting vertex

    print("Edge \tWeight")
    for _ in range(self.size):
      u = min((v for v in range(self.size) if not in_mst[v]), key=lambda v: key_values[v])

      in_mst[u] = True

      if parents[u] != -1:  # Skip printing for the first vertex since it has no parent
        print(f"{self.vertex_data[parents[u]]}-{self.vertex_data[u]} \t{self.adj_matrix[u][parents[u]]}")

      for v in range(self.size):
        if 0 < self.adj_matrix[u][v] < key_values[v] and not in_mst[v]:
          key_values[v] = self.adj_matrix[u][v]
          parents[v] = u


# ---------------------------------------------------------

graph = Graph(8)

graph.add_vertex_data(0, 'A')
graph.add_vertex_data(1, 'B')
graph.add_vertex_data(2, 'C')
graph.add_vertex_data(3, 'D')
graph.add_vertex_data(4, 'E')
graph.add_vertex_data(5, 'F')
graph.add_vertex_data(6, 'G')
graph.add_vertex_data(7, 'H')

graph.add_edge(0, 1, 4)  # A - B
graph.add_edge(0, 3, 3)  # A - D
graph.add_edge(1, 2, 3)  # B - C
graph.add_edge(1, 3, 5)  # B - D
graph.add_edge(1, 4, 6)  # B - E
graph.add_edge(2, 4, 4)  # C - E
graph.add_edge(2, 7, 2)  # C - H
graph.add_edge(3, 4, 7)  # D - E
graph.add_edge(3, 5, 4)  # D - F
graph.add_edge(4, 5, 5)  # E - F
graph.add_edge(4, 6, 3)  # E - G
graph.add_edge(5, 6, 7)  # F - G
graph.add_edge(6, 7, 5)  # G - H

print("Prim's Algorithm MST:")
graph.prims_algorithm()

