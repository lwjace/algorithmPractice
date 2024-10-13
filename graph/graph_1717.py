import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
parent = [0] * (N+1)

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def