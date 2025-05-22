# KNN Graph

import math
import random
from collections import defaultdict


def rnd(low=1, high=10):
  return random.randint(low, high)

def dist(p1, p2):
  acc = 0
  for i in range(len(p1)):
    acc += (p1[i] - p2[i])**2
  return math.sqrt(acc)

def nearest_neighbor_graph(points, k):
  graph = defaultdict(list)
  for i in range(len(points)):
    distances = []
    for j in range(len(points)):
      if i != j:
        distances.append((dist(points[i], points[j]), j))
    distances.sort()
    for l in range(min(k, len(distances))):
      neighbor_index = distances[l][1]
      graph[i].append(neighbor_index)
  return dict(graph)


# ---------------------------------------------------------

#points = [[1, 2], [3, 4], [5, 6], [7, 8], [2, 1], [4, 3]]
points = [(rnd(),rnd()) for _ in range(6)]
k = 2
graph = nearest_neighbor_graph(points, k)
print(graph)
