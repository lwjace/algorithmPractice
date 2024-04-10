import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
visit = [False] * (n +1)

def dfs (i) :
    visit[i] = True
    for r in a[i]:
        if not visit[r] :
            dfs(r)

for _ in range(m):
    s, e = map(int, input().split())
    a[e].append(s)
    a[s].append(e)

count = 0

for i in range(1, n+1):
    if not visit[i]:
        count += 1
        dfs(i)

print(count)
    
