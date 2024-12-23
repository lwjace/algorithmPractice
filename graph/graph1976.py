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
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(1, N+1):
    dosi[i] = list(map(int, input().split()))
    dosi[i].insert(0, 0)

route = list(map(int, input().split()))