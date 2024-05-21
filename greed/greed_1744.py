from queue import PriorityQueue
N = int(input())
plusPq = PriorityQueue()
minusPq = PriorityQueue()
one = 9
zero = 0

for i in range(N):
    data = int(input())
    if data > 1:
        