ufnode = dict()
parent = []
size = []

# NO DUPLICATE VALS
def make_ufnode(val):
    if val in ufnode: raise Exception
    i = len(ufnode)
    ufnode[val] = i
    parent.append(i)
    size.append(1)

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a_root, b_root = find(a), find(b)
    if a_root != b_root:
        if size[a_root] < size[b_root]:
            a_root, b_root = b_root, a_root
        parent[b_root] = a_root
        size[a_root] += size[b_root]

def ufsets():
    from collections import defaultdict
    hm = defaultdict(list)
    for val, node in ufnode.items():
        hm[find(node)].append(val)
    return dict(hm)


arr = [100, 200, 300, 400, 500]
for x in arr:
    make_ufnode(x)

print(ufnode)
union(ufnode[100], ufnode[200])
union(ufnode[400], ufnode[500])
print(parent)
print(size)
union(ufnode[200], ufnode[500])
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
