"""
Sparse table implementation
"""
import math
N = 100
K = int(math.ceil(math.log(N+1,2)))
RMQ = [[0 for _ in range(K)] for _ in range(N)]


def build(arr):
    for i in range(N):
        RMQ[i][0] = arr[i]
    for k in range(1, K):
        for i in range(0, N-2**k+1):
            RMQ[i][k] = min(RMQ[i][k-1], RMQ[i+2**(k-1)][k-1])

# inclusive, exclusive
def rmquery(i, j):
    length = j-i
    if length == 0: return None
    k = int(math.floor(math.log(length,2)))
    left = RMQ[i][k]
    right = RMQ[j-2**k][k]
    return min(left, right)


# TEST
"""
import random
seed = random.randint(0, 100)
print("seed", seed)
random.seed(seed)
# arr = list(range(1, N+1))
arr = [random.randint(0, 100) for _ in range(N)]

build(arr)

rmins = dict()
for i in range(N):
    for j in range(i, N):
        rmin = min(arr[i:j+1])
        rmins[(i,j+1)] = rmin

for i in range(N):
    for j in range(i+1, N+1):
        if rmquery(i,j) != rmins[(i,j)]:
                print(i, j, rmquery(i,j), rmins[(i,j)])
"""

# https://judge.yosupo.jp/problem/staticrmq
import math
_, Q = input().split()
arr = list(map(int, input().split()))
N = len(arr)
K = int(math.ceil(math.log(N+1,2)))
RMQ = [[0 for _ in range(K)] for _ in range(N)]
build(arr)
for _ in range(int(Q)):
    l, r = map(int, input().split())
    print(rmquery(l,r))
