#imports
import sys
import copy
import operator
import math
import collections
import heapq
import itertools
import functools
import bisect
import sortedcontainers
# import pqdict
from pprint import pprint

[[0]*n for _ in range(m)] # generate m x n array
[[[0 for _ in range(k)] for _ in range(j)] for _ in range(i)] # generate i x j x k array

matrix_t = map(list, zip(*matrix))        # transpose matrix
matrix_r = map(list, zip(*matrix[::-1]))  # rotate matrix cw - flip ud, then transpose
matrix_r = map(list, zip(*matrix)[::-1])  # rotate matrix ccw - transpose, then flip ud
matrix_r = [a[::-1] for a in m[::-1]]     # rotate matrix 180 - flip ud, then flip lr
points = zip(x_values, y_values)          # zip lists to get tuples at each index
[x for b in a for x in b]                 # flatten 2-d list

# string
s.isalpha()    # check if all chars in str are in alphabet
s.isalnum()    # check if all chars in str are alphanumeric
s.isdecimal()  # check if all chars in str are digits
s.isupper()    # check if all uppercase
s.upper()      # return all uppercase
s.find()       # find leftmost index containing substring
s.rfind()      # find rightmost index containing substring

# binary tricks
format(x, 'b')     # int to binary string
format(x, '08b')   # int to binary string with 8 digits
int('10101', 2)    # binary string to int
itertools.product([0,1], repeat=n)  # all bitstrings of length n

# itertools
itertools.product("01", repeat=n)  # all bitstrings of length n
itertools.combinations(list, n)    # n-tuples of list in original order

# helpful
a, b = b, a  # swap elements
field1, field2 = map(d.get, ["field1", "field2"])  # map dict values to variable name
(3, 3) > (3, 2) # tuple comparison to break ties for key=
l = l[::-1] # reverse list
# list: count(), index()
# set: discard()
# enumerate

# deque: 
# append(), pop(), appendleft(), popleft()
# rotate(n=1) - rotate n to the right (negative n to the left)

# Counter:
# most_common([n]) - n number of (element, count) from most common to least

# heapq: minheap, use negative priority for maxheap
# heapq.heappush(h, (priority, item), heapq.heappop()
# heapq.heapify(), heapq.nlargest(n, iterable[, key]), heapq.nsmallest(n, iterable[, key])
# treeset/treemap - use maxheap + minheap + invalidated set or sortedcontainers
# minq - monotonically increasing, append by popping while back is greater before appending
# maxq - monotonically decreasing, append by popping while back is lesser before appending

# bisect cases
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect.bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

# bsearch:
# to find smallest index satisfying predicate 'gte num' - mid = (hi+lo)/2, if mid >= num: hi = mid, else: lo = mid+1
def bsearch(num, lo, hi):
    while lo < hi:
        mid = (lo + hi) / 2
        if mid >= num:
            hi = mid
        else:
            lo = mid+1
    if lo < num: return -1
    return lo

# to find largest index satisfying predicate 'lte num' - mid = (hi+lo+1)/2, if mid <= num: lo = mid, else: hi = mid-1
def bsearch(num, lo, hi):
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if mid <= num:
            lo = mid
        else:
            hi = mid-1
    if lo > num: return -1
    return lo


""" Graph """
dxdy4 = [(1,0),(-1,0),(0,1),(0,-1)]
dxdy8 = [d for d in itertools.product([-1,0,1], repeat=2) if d != (0,0)]
def bfs(v, A):
    M, N = len(A), len(A[0])
    visited = set()
    q = deque()
    q.append((v,0))
    while q:
        v, dist = q.popleft()
        if v in visited: continue
        visited.add(v)
        x, y = v
        for dx, dy in dxy4:
            if 0 <= x+dx < M and 0 <= y+dy < N:
                q.append(((x+dx,y+dy), dist+1))

def neigh(i, j):
    res = [(i+dx, j+dy) for dx, dy in dxy4 if 0 <= i+dx < M and 0 <= j+dy < N]
    return res

""" Number Theory """
pow(a, b, c) # equals a^b mod c

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def is_prime(X):
    import math
    s = int(math.floor(math.sqrt(X)))
    for a in range(2, s+1):
        if X % a == 0: 
            return False
    return True

def nCk(n, k):
    if k == 0: return 1
    return n * nCk(n-1, k-1) / k

# DP
"""Find a contiguous subarray with the largest sum."""
def max_subarray(numbers):
    best_sum = 0
    best_start = best_end = 0
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            current_start = current_end
            current_sum = x
        else:
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1

    return best_sum, best_start, best_end
