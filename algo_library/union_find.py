node_to_index = dict()
index_to_node = []
parent = []
size = []

# NO DUPLICATE NODES
def make_ufnode(node):
    if node in node_to_index: raise Exception
    i = len(node_to_index)
    node_to_index[node] = i
    index_to_node.append(node)
    parent.append(i)
    size.append(1)

def find(a):
    return index_to_node[_find(node_to_index[a])]

def union(a, b):
    _union(node_to_index[a], node_to_index[b])

def ufsets():
    import collections
    hm = collections.defaultdict(list)
    for node, idx in node_to_index.items():
        hm[find(node)].append(index_to_node[idx])
    return dict(hm)

def _find(a):
    if parent[a] == a:
        return a
    parent[a] = _find(parent[a])
    return parent[a]

def _union(a, b):
    a_root, b_root = _find(a), _find(b)
    if a_root != b_root:
        if size[a_root] < size[b_root]:
            a_root, b_root = b_root, a_root
        parent[b_root] = a_root
        size[a_root] += size[b_root]


arr = [100, 200, 300, 400, 500]
for x in arr:
    make_ufnode(x)
print(node_to_index)
union(100, 200)
union(400, 500)
print(parent)
print(size)
union(200, 500)
print(parent)
print(size)
print(ufsets())

"""
class ufnode:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.size = 1

def find(a):
    if a.parent == a:
        return a
    a.parent = find(a.parent)
    return a.parent

def union(a, b): 
    a_root, b_root = find(a), find(b)
    if a_root != b_root:
        if a_root.size < b_root.size:
            a_root, b_root = b_root, a_root
        b_root.parent = a_root
        a_root.size += b_root.size
"""
