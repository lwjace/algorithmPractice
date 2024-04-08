# https://www.acmicpc.net/problem/11003
from collections import deque
N, L = map (int, input().split())
mdeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    while mdeque and mdeque[-1][0] > now[i]:
        mdeque.pop()
    mdeque.append((now[i], i))
    if mdeque[0][1] <= i - L:
        mdeque.popleft()
    print(mdeque[0][0], end = ' ')