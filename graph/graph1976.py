N = int(input())
M = int(input())
dosi = [[0 for j in ragne(N+a)] for i in range(N+1)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):