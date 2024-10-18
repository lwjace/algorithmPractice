import sys
sys.stdin = open ("input.txt", "rt")
n, k = map(int, input().split()) #값 읽어오기

cnt = 0

for i in range(1, n+1):
    if (n % i == 0):
        cnt += 1
        if (cnt == k):
            print(k)
            break
else: 
    print(-1)    
