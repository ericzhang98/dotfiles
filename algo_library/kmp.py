"""
KMP string searching algorithm
Finds occurrences of pattern P in text T

construct DFA transition table using a lagging state
follow transition table

prefix function - pi[i] = arg max k<=i s.t. T[0:k] = T[i+1-k:i+1]
i.e. length of largest strict prefix that is also a suffix for T[0:i+1], the substring ending at index i
pi[-1] = 0
pi[0] = 0
pi[1] = 1 if T[0] == T[1] else 0

"""

def prefix_function(S):
    prefix = [0]
    curr_prefix = 0
    for i in range(1, len(S)):
        while curr_prefix > -1 and S[i] != S[curr_prefix]:
            curr_prefix = prefix[curr_prefix-1] if curr_prefix > 0 else -1
        curr_prefix += 1
        prefix.append(curr_prefix)
    return prefix

def KMP_prefix(P, T):
    M, N = len(P), len(T)
    S = P + "#" + T
    pi = prefix_function(S)
    pi = pi[M+1:]
    start_indices = []
    for i in range(N):
        if pi[i] == M:
            start_indices.append(i-M+1)
    return start_indices

def string_automaton(P):
    P += "#"
    alphabet = [chr(ord('a') + i) for i in range(26)] + ['#']
    M, N = len(P), len(alphabet)
    transition_table = [[0] * N for _ in range(M)]
    pi = prefix_function(P)
    for i in range(0, M):
        for j in range(N):
            if P[i] == alphabet[j]:
                transition_table[i][j] = i + 1
            else:
                if i > 0:
                    transition_table[i][j] = transition_table[pi[i-1]][j]
                else:
                    transition_table[i][j] = 0
    return transition_table

def KMP_table(P, T):
    M, N = len(P), len(T)
    chr_idx = {chr(ord('a') + i): i for i in range(26)}
    transition_table = string_automaton(P)
    start_indices = []
    curr_state = 0
    for i in range(N):
        c = chr_idx[T[i]]
        curr_state = transition_table[curr_state][c]
        if curr_state == M:
            start_indices.append(i-M+1)
    return start_indices

assert prefix_function("aaaaa") == [0,1,2,3,4]
assert KMP_prefix("aa", "aaaaa") == [0,1,2,3]
assert KMP_table("aa", "aaaaa") == [0,1,2,3]
