import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
A = [[] for _ in range(N+1)]
answer = [0] * (N+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                queue.append(i)