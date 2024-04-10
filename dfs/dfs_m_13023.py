import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())


rel = [[] for _ in range (N+1)]
visited = [False] * (N+1)
flag = False
def dfs(now, depth):
    global flag 
    if depth == 5:
        flag = True
        print(1)
        return
    
    visited[now] = True
    for i in rel[now]: # 헤깔리던 부분
        if not visited[i] :    #틀린 부분 rel이 아니라 visited임
           dfs(i, depth + 1) # 헤깔리던 부분
    visited[now] = False # 생각 못한 부분 -> 하나에 대한 관계 확인이 끝나면 다음 것을 보기 위해 초기화 필요
    return

for _ in range (M):
    s, e = map(int, input().split())
    rel[s].append(e)
    rel[e].append(s)

for i in range(N):
    dfs(i,1)
    if flag:
        break

if not flag:
    print (0)
#else :
#    print(1)