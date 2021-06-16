# Successive shortest path algorithm - https://cp-algorithms.com/graph/min_cost_flow.html
# O(V^2*E^2)

import collections, heapq

def bellman_ford(graph, costs, V, source, sink):
    dist = collections.defaultdict(lambda: float('inf'))
    prv = {}
    dist[source] = 0
    # relaxation -- min-cost k-length path at each kth iteration 
    for _ in range(V-1):
        for u in graph:
            for v in graph[u]:
                if graph[u][v] > 0:
                    if dist[u] + costs[u][v] < dist[v]:
                        dist[v] = dist[u] + costs[u][v]
                        prv[v] = u
    # negative cycles can occur, but thats ok, so don't check
    if dist[sink] == float('inf'):
        return False, [] # sink unreachable
    path = collections.deque()
    v = sink
    while v != source:
        path.appendleft((prv[v], v))
        v = prv[v]
    return True, path

# only works on flow networks with single directional flows
# make sure graph and cost are collections.defaultdict(lambda: collections.defaultdict(int))
# graph[u][v] = capacity of edge
# costs[u][v] = cost per unit flow
# edits the graph by maintaining it as residual graph
def min_cost_flow(graph, costs, source, sink, desired_flow=float('inf')):
    pairs = []
    for u in list(costs):
        for v in list(costs[u]):
            costs[v][u] = -costs[u][v]
    min_cost = 0
    curr_flow = 0
    # augment the flow while less than desired flow by pushing flow from 
    while curr_flow < desired_flow:
        residual_flow_exists, residual_path = bellman_ford(graph, costs, len(costs), source, sink)
        if not residual_flow_exists:
            return curr_flow, min_cost
        residual_capacity = min(graph[u][v] for u, v in residual_path)
        residual_capacity = min(residual_capacity, desired_flow - curr_flow) # upper bound additional flow by remaining delta before desired flow
        curr_flow += residual_capacity
        # update residual graph and min_cost
        for u, v in residual_path:
            graph[u][v] -= residual_capacity
            graph[v][u] += residual_capacity
            min_cost += residual_capacity * costs[u][v]
    return curr_flow, min_cost
            
"""
# manual testing
G = collections.defaultdict(lambda: collections.defaultdict(int))
C = collections.defaultdict(lambda: collections.defaultdict(int))
s, t = 's', 't'
G[s][0] = 10
G[0][t] = 8
G[s][1] = 5
G[1][t] = 7
G[0][1] = 100
C[s][0] = 1
C[0][t] = 1
C[s][1] = 1
C[1][t] = 1
C[0][1] = 1
print(min_cost_flow(G,C,s,t)) # should be (15, 32)
"""

"""
# manual testing
G = collections.defaultdict(lambda: collections.defaultdict(int))
C = collections.defaultdict(lambda: collections.defaultdict(int))
s, t = 0, 3
desired_flow = 2
G[0][1] = 2
G[0][2] = 1
G[1][2] = 1
G[1][3] = 1
G[2][3] = 2
C[0][1] = 1
C[0][2] = 2
C[1][2] = 1
C[1][3] = 3
C[2][3] = 1
print(min_cost_flow(G,C,s,t,desired_flow)[1]) # should be 6
"""

"""
# tested: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_6_B
n, m, desired_flow = list(map(int, input().split()))
G = collections.defaultdict(lambda: collections.defaultdict(int))
C = collections.defaultdict(lambda: collections.defaultdict(int))
for _ in range(m):
    u, v, c, d = list(map(int, input().split()))
    G[u][v] = c
    C[u][v] = d
max_flow, min_cost = min_cost_flow(G, C, 0, n-1, desired_flow)
if max_flow == desired_flow:
    print(min_cost)
else:
    print(-1)
"""
