import math
N = int(input())
A = [0] * (10000001)

for i in range(2, len(A)):
    A[i] = i
for i in range(2, int(math.sqrt(len(A))+1)):
    