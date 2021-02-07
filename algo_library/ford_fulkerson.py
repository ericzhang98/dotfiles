# Ford-Fulkerson algorithm - https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
# O(Ef), where f is max potential flow

import collections

def residual_graph(G, f):
    Gf = collections.defaultdict(lambda: collections.defaultdict(int))
    for u in G:
        for v, capacity in G[u].items():
            Gf[u][v] = capacity
    for (u, v), flow in f.items():
        Gf[u][v] -= flow
        Gf[v][u] = flow
    return Gf

def residual_flow_path(Gf, s, t):
    visiting = set()
    def dfs(u):
        if u == t: return float('inf'), []
        if u in visiting: return 0, []
        visiting.add(u)
        for v, capacity in Gf[u].items():
            if capacity > 0:
                remaining_capacity, remaining_path = dfs(v)
                if remaining_capacity > 0:
                    return min(capacity, remaining_capacity), [(u,v)] + remaining_path
        return 0, []
    return dfs(s)

# make sure G is collections.defaultdict(lambda: collections.defaultdict(int))
# graph[u][v] = capacity
# edits the graph by maintaining it as residual graph
def ford_fulkerson(G, s, t):
    f = collections.defaultdict(int)
    max_flow = 0
    while True:
        Gf = residual_graph(G, f)
        residual_flow, residual_path = residual_flow_path(Gf, s, t)
        if residual_flow == 0: return max_flow
        for u, v in residual_path:
            f[(u,v)] += residual_flow
        max_flow += residual_flow


"""
# tested: https://www.hackerearth.com/practice/algorithms/graphs/min-cut/tutorial/
N, X, Y = input().split(" ")
G = collections.defaultdict(lambda: collections.defaultdict(int))
for _ in range(int(N)):
    V_i, V_j, capacity = input().split(" ")
    G[V_i][V_j] = int(capacity)
    G[V_j][V_i] = int(capacity)

print(ford_fulkerson(G, X, Y))
"""

"""
# tested correct but tle: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_6_A
n, m = list(map(int, input().split()))
G = collections.defaultdict(lambda: collections.defaultdict(int))
for _ in range(m):
    u, v, c = list(map(int, input().split()))
    G[u][v] = c

print(ford_fulkerson(G, 0, n-1))
"""
