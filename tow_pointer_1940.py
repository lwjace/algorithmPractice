#https://www.acmicpc.net/problem/1940

import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
a = sorted(list(map(int, input().split())))

sp = 0
ep = n-1
answer = 0

while sp < ep :
    sum = a[sp] + a[ep]
    if sum < m :
        sp += 1
    elif sum > m :
        ep -= 1
    else :
        answer += 1
        sp += 1
        ep -= 1


print(answer)

