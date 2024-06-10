import math
Min, Max = map(int, input().split())
A = [0] * (1000001)

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A))+1)):
    if A[i] == 0:
        continue
    for j in range(i+i, len(A), i):
        A[j] = 0