from collections import deque

Sender = [0, 0, 1, 1, 2, 2]
Receiver = [1, 2, 0, 2, 0, 1]
now = list(map(int, input().split()))
visited = [[False for j in range(201)] for i in range(201)]