# Global mincut - https://en.wikipedia.org/wiki/Stoer%E2%80%93Wagner_algorithm
def mincut_phase(weights, arb):
    X = [arb]
    while len(X) != len(weights):
        cutsize, tcv = max((sum(weights[v].get(xv, 0) for xv in X), v) for v in weights if v not in X)
        X.append(tcv)
    s, t = X[-2], X[-1]
    for ne in weights[t]:
        if ne == s: continue
        weights[s][ne] += weights[t][ne]
        weights[ne][s] = weights[s][ne]
        if t in weights[ne]: del weights[ne][t]
    del weights[t]
    if t in weights[s]: del weights[s][t]
    return cutsize
        
def global_mincut(weights):
    arb = list(weights.keys())[0]
    ans = float('inf')
    while len(weights) > 1:
        cutsize = mincut_phase(weights, arb)
        ans = min(cutsize, ans)
    return ans
