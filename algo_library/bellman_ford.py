# Bellman-Ford algorithm - https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
# O(VE)

import collections

# graph must be collections.defaultdict(dict)
# G[u][v] = weight
# V = num vertices
def bellman_ford(G, V, source):
    dist = collections.defaultdict(lambda: float('inf'))
    prv = {}
    dist[source] = 0
    # relaxation -- min-cost k-length path at each kth iteration 
    for _ in range(V-1):
        for u in G:
            for v in G[u]:
                if dist[u] + G[u][v] < dist[v]:
                    dist[v] = dist[u] + G[u][v]
                    prv[v] = u
    for u in G:
        for v in G[u]:
            if dist[u] + G[u][v] < dist[v]:
                # contains negative cycle
                # cycle can be constructed by going back n predecessors to get a node in cycle
                # then repeatedly going back precedecessors until reaching itself
                prv[v] = u
                curr = v
                for _ in range(V):
                    curr = prv[curr]
                cycle = []
                fixed_node = curr
                while True:
                    cycle.append(curr)
                    curr = prv[curr]
                    if curr == fixed_node:
                        break
                return dist, prv, cycle
    return dist, prv, None

"""
# tested: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_1_B
V, E, source = map(int, input().split())
G = collections.defaultdict(dict)
for _ in range(E):
    u, v, d = map(int, input().split())
    G[u][v] = d
dist, prv, cycle = bellman_ford(G, V, source)
if cycle is None:
    for v in range(V):
        if dist[v] == float('inf'):
            print("INF")
        else:
            print(dist[v])
else:
    print("NEGATIVE CYCLE")
"""
