import sys
import math
from collections import defaultdict, Counter
import heapq
import copy

def image_of_file(f):
    indexes = [i for i in range(len(f)) if f[i] == '_']
    return f[:indexes[-2]]

def solution(args):
    idx = args.index('')
    images = set( args[:idx])
    unused = copy.copy(images)
    files = args[idx+1:]
    orphans = []

    for f in files:
        image = image_of_file(f)
        if image in images:
            unused.discard(image)
        else:
            orphans.append(f)

    if len(unused) == 0 and len(orphans) == 0:
        print("No mismatches.")
        return

    eprint("test")

    for l in sorted(orphans):
        print("F", l)
    for l in sorted(list(unused)):
        print("I", l)


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

params = []
while True:
    try:
        line = input()
    except:
        break
    params.append(line)

solution(params)
