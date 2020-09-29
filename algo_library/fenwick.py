"""
Fenwick Tree / Binary Indexed Tree

Allows for modification of values in array and range sum computation in logn time
"""
N = 1000
BIT = [0 for _ in range(N)]

def update(i, val):
    i += 1
    while i <= N:
        BIT[i-1] += val
        i += (i & -i)

def query(i):
    csum = 0
    while i > 0:
        csum += BIT[i-1]
        i -= (i & -i)
    return csum

# computes sum(a[i:j])
def rangequery(i, j):
    return query(j) - query(i)


# TEST
import random
seed = random.randint(0, 100)
print("seed", seed)
random.seed(seed)
# arr = list(range(1, N+1))
arr = [random.randint(0, 100) for _ in range(N)]

csums = dict()
for i in range(N):
    csum = 0
    csums[(i,i)] = csum
    for j in range(i, N):
        csum += arr[j]
        csums[(i,j+1)] = csum

for i in range(N):
    update(i, arr[i])

for i in range(N):
    for j in range(i, N+1):
        if rangequery(i,j) != csums[(i,j)]:
            print("ERR")
            print(i, j, csums[(i,j)], rangequery(i,j))
