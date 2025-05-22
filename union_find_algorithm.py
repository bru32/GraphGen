# Union-Find Algorithm
# source:
#   ByteVigor - Union Find Visually Explained
#   https://www.youtube.com/watch?v=92UpvDXc8fs&list=PLZ1XikRjVdB6bMxkZOfN3Y_p02z6GiIsk&index=4
# Edited by Bruce Wernick
# 19 May 2025


class UnionFind:
  def __init__(self, n):
    self.parent = list(range(n))
    self.rank = [0]*n  # for union by rank

  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])  # Path compression
    return self.parent[x]

  def union(self, x, y):
    x0 = self.find(x)
    y0 = self.find(y)
    if x0 == y0:
      return False
    if self.rank[x0] < self.rank[y0]:
      self.parent[x0] = y0
    elif self.rank[x0] > self.rank[y0]:
      self.parent[y0] = x0
    else:
      self.parent[y0] = x0
      self.rank[x0] += 1
    return True

