from collections import deque
N, M, start = map(int, input().split())
A = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

visited = [False] * (N+1)


for i in range(N+1):
    A[i].sort()

def dfs (num):
    print(num, end =' ')
    visited = True
    for i in A[num]:
        if not visited[i]:
            dfs(i)

dfs(start)

def BFS(V):
    queue = deque()
    queue.append(V)
    visited[V] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end= ' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
print()
visited = [False] * (N+1)
BFS(start)