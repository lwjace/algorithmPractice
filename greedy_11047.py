N, K = map(int, input().split())
AB = [0] * N

for i in range(N):
    AB[i] = int(input())

count = 0

for i in range(N-1, -1, -1):
    if AB[i] <= K:
        count += int(K/AB[i])
        K= K%AB[i]
print(count)
