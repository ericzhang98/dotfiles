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

def make_coloring(edges):
    coloring = [[], []]
    visited = set()
    def dfs(u, color):
        if u in visited:
            return
        visited.add(u)
        coloring[color].append(u)
        for v in edges[u]:
            dfs(v, 1-color)
    for u in edges:
        dfs(u, 0)
    return coloring

# max_bipartite_matching == min_vertex_cover == n - max_independent_set
# make sure edges has every vertex as a key
def max_bipartite_matching(edges):
    coloring = make_coloring(edges)
    source, sink = "source", "sink"
    graph = collections.defaultdict(lambda: collections.defaultdict(int))
    for u in coloring[0]:
        graph[source][u] = 1
    for v in coloring[1]:
        graph[v][sink] = 1
    for u in coloring[0]:
        for v in edges[u]:
            graph[u][v] = 1
    return dinics(graph, source, sink)

# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_7_A
"""
X, Y, E = map(int, input().split())
edges = {}
for x in range(X):
    edges[f"x_{x}"] = []
for y in range(Y):
    edges[f"y_{y}"] = []
for _ in range(E):
    x, y = map(int, input().split())
    edges[f"x_{x}"].append(f"y_{y}")
    edges[f"y_{y}"].append(f"x_{x}")

print(max_bipartite_matching(edges))
"""
