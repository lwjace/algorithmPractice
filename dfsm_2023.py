import sys
input = sys.stdin.readline

n = int(input())

prime = []

def isprime(v):
    for i in v:
        if v % i != 0:
            return False
    prime.append(v)
    return True

def dfs(num):
    if len(str(num)) == n:
        