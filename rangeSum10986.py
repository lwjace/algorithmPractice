import sys
input = sys.stdin.readline

n, m = map(int, input().split())
origin = list(map(int, input().split()))
sum = [0] * n 
rNum = [0] * m
answer = 0
sum[0] = origin[0]

for i in range(1, n):
    sum[i] = sum[i-1] + origin[i]

for i in range(n):
    remainder = sum[i] % m
    if remainder == 0 :
        answer += 1
    rNum[remainder] += 1

for i in range(m):
    if rNum[i] > 1:
        answer += (rNum[i] * (rNum[i] -1) // 2 )

print(answer)