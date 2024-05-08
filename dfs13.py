import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
arrive = FalseA = [[] for _ in range(N+1)]

def DFS(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    