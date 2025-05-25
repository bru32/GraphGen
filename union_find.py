# Union-Find Closure
# zero based

def make_union_find(size):
  parent = list(range(size))
  rank = [0]*size

  def find(x):
    if parent[x] != x:
      parent[x] = find(parent[x])
    return parent[x]

  def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root:
      return
    if rank[x_root] < rank[y_root]:
      parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
      parent[y_root] = x_root
    else:
      parent[y_root] = x_root
      rank[x_root] += 1

  return union, find

# ---------------------------------------------------------

edges = [(0,1),(1,2),(3,4),(0,3)]
n = max(max(u,v) for u,v in edges)+1
union, find = make_union_find(n)
for u, v in edges:
  union(u, v)
u, v = 0, 3
a, b = find(u), find(v)
print(f"root({u})={a}")
print(f"root({v})={b}")
