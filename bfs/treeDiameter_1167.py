from collections import deque

N = int(input())
A = [[] for _ in range(N+1)]

for _ in range(N):
    Data = list(map(int, input().split()))
    a = Data[0]
    index = 1
    while True:
        v = Data[index] 
        if v == -1:
            break
        s = Data[index+1]
        A[a].append((v,s))
        index += 2

distance = [0] * (N+1)
visit = [False] * (N+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visit[v] = True
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if not visit[i[0]]:
                visit[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now] + i[1]

BFS(1)
Max = 1

for i in range(2, N+1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (N+1)
visit = [False] * (N+1)
BFS(Max)
distance.sort()
print(distance[N])

