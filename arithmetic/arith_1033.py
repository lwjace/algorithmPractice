N = int(input())
A = [[] for _ in range(N)]
visited = [False] * (N)
D = [0] * (N)
lcm = 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        next = i[0]
        if not visited[next]:
            D[next] = D[v] * i[2] // i[1]
            DFS(next)