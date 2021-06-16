# min cost bipartite matching via min cost flow
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

# edges must be a dict mapping vertex -> [neighbors] -> cost
# left and right are lists of the 2 disjoint sets
def min_cost_bipartite_matching(edges, left, right):
    source, sink = "source", "sink"
    graph = collections.defaultdict(lambda: collections.defaultdict(int))
    costs = collections.defaultdict(lambda: collections.defaultdict(int))
    for u in left:
        graph[source][u] = 1
        costs[source][u] = 0
    for v in right:
        graph[v][sink] = 1
        costs[v][sink] = 0
    for u in left:
        for v in edges[u]:
            graph[u][v] = 1
            costs[u][v] = edges[u][v]
    return min_cost_flow(graph, costs, source, sink)

"""
# tested: https://www.hackerearth.com/practice/algorithms/graphs/minimum-cost-maximum-flow/tutorial/
n = int(input())
edges = collections.defaultdict(lambda: collections.defaultdict(int))
for i in range(n):
    for j, cost in enumerate(map(int, input().split())):
        edges[f"worker_{i}"][f"task_{j}"] = cost
left = [f"worker_{i}" for i in range(n)]
right = [f"task_{j}" for j in range(n)]
max_flow, min_cost = min_cost_bipartite_matching(edges, left, right)
print(min_cost)
"""
