# Dinic's algorithm - https://en.wikipedia.org/wiki/Dinic%27s_algorithm
# O(V^2E) for general flow networks, O(V^0.5E) for unit networks e.g. solving maximum bipartite matching

import collections

def construct_layered_graph(graph, source):
    layered_graph = collections.defaultdict(lambda: collections.defaultdict(int))
    dists = {source: 0}
    queue = collections.deque([(source, dists[source])])
    while queue:
        u, dist = queue.popleft()
        for v, capacity in graph[u].items():
            if capacity > 0:
                if v not in dists:
                    dists[v] = dist+1
                    queue.append((v, dists[v]))
                if dists[v] == dists[u]+1:
                    layered_graph[u][v] = capacity
    return layered_graph

def find_blocking_flow(layered_graph, source, sink):
    # layered graphs are acyclic, arbitrarily push flow when possible during dfs
    blocking_flow = collections.defaultdict(int)
    def dfs(u, pullable_flow_u):
        if u == sink:
            return pullable_flow_u
        pushable_flow_u = 0
        for v, capacity in list(layered_graph[u].items()):
            pullable_flow_v = min(pullable_flow_u, layered_graph[u][v])
            pushable_flow_v = dfs(v, pullable_flow_v)
            pushable_flow_u += pushable_flow_v
            pullable_flow_u -= pushable_flow_v
            blocking_flow[(u, v)] += pushable_flow_v
            layered_graph[u][v] -= pushable_flow_v
            if layered_graph[u][v] == 0:
                del layered_graph[u][v]
        return pushable_flow_u
    pushed_flow = dfs(source, float('inf'))
    return pushed_flow, blocking_flow

# make sure graph is collections.defaultdict(lambda: collections.defaultdict(int))
# graph[u][v] = capacity
# edits the graph by maintaining it as residual graph
def dinics(graph, source, sink):
    max_flow = 0
    # augment the flow by a blocking flow in the layered resdiual graph
    while True:
        layered_graph = construct_layered_graph(graph, source)
        pushed_flow, blocking_flow = find_blocking_flow(layered_graph, source, sink)
        if pushed_flow == 0:
            return max_flow
        max_flow += pushed_flow
        for (u, v), fuv in blocking_flow.items():
            graph[u][v] -= fuv
            graph[v][u] += fuv

# manual testing
"""
G = collections.defaultdict(lambda: collections.defaultdict(int))
s, t = 's', 't'
G[s][0] = 10
G[0][t] = 8
G[s][1] = 5
G[1][t] = 7
G[0][1] = 100
print(dinics(G,s,t))
"""

# tested: https://www.hackerearth.com/practice/algorithms/graphs/min-cut/tutorial/
"""
N, X, Y = input().split(" ")
G = collections.defaultdict(lambda: collections.defaultdict(int))
for _ in range(int(N)):
    V_i, V_j, capacity = input().split(" ")
    G[V_i][V_j] = int(capacity)
    G[V_j][V_i] = int(capacity)

print(dinics(G, X, Y))
"""

# tested: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_6_A
"""
n, m = list(map(int, input().split()))
G = collections.defaultdict(lambda: collections.defaultdict(int))
for _ in range(m):
    u, v, c = list(map(int, input().split()))
    G[u][v] = c

print(dinics(G, 0, n-1))
"""
