import sys
input = sys.stdin.readline

n = int(input())

prime = []

def isprime(v):
    for i in range(2, int((v / 2) +1) ):
        if v % i == 0:
            return False
    prime.append(v)
    return True

def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(1, 10):
            if isprime(num * 10 + i):
                dfs(num * 10 + i)
dfs(2)
dfs(3)
dfs(5)
dfs(7)