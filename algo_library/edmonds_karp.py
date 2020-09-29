# Edmonds-Karp algorithm - https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm
# O(VE^2)

import collections

# returns true if there is a path from source to sink in residual graph and stores path backwards in prv
def bfs(graph, source, sink):
    visited = {source}
    prv = {}
    queue = collections.deque([source])
    while queue:
        u = queue.popleft()
        for v, capacity in graph[u].items():
            if v not in visited and capacity > 0:
                queue.append(v)
                visited.add(v)
                prv[v] = u
    if sink not in visited: return False, []
    path = collections.deque()
    v = sink
    while v != source:
        path.appendleft((prv[v], v))
        v = prv[v]
    return True, path

# make sure graph is collections.defaultdict(lambda: collections.defaultdict(int))
def edmonds_karp(graph, source, sink):
    max_flow = 0
    # augment the flow while there is path from source to sink in residual graph
    while True:
        residual_flow_exists, residual_path = bfs(graph, source, sink)
        if not residual_flow_exists: return max_flow
        residual_capacity = min(graph[u][v] for u, v in residual_path)
        max_flow += residual_capacity
        # update residual graph
        for u, v in residual_path:
            graph[u][v] -= residual_capacity
            graph[v][u] += residual_capacity

"""
# tested: https://www.hackerearth.com/practice/algorithms/graphs/min-cut/tutorial/
N, X, Y = input().split(" ")
G = collections.defaultdict(lambda: collections.defaultdict(int))
for _ in range(int(N)):
    V_i, V_j, capacity = input().split(" ")
    G[V_i][V_j] = int(capacity)
    G[V_j][V_i] = int(capacity)

print(edmonds_karp(G, X, Y))
"""

"""
# tested: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_6_A
n, m = list(map(int, input().split()))
G = collections.defaultdict(lambda: collections.defaultdict(int))
for _ in range(m):
    u, v, c = list(map(int, input().split()))
    G[u][v] = c

print(edmonds_karp(G, 0, n-1))
"""
