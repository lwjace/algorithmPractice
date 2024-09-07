import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
IsEven = True

def DFS(node):
    global IsEven
    visited[node] = True
    for i in A[node]:
        if not visited[i]:
            check[i] = (check[node]+1)%2
            DFS(i)
        elif check[node] == check[i]:
            IsEven = False

for _ in range(N):
    V, E = map(int, input().split())
    A = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    check = [0] * (V + 1)
    IsEven =True
    