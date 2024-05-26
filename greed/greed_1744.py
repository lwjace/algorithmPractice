from queue import PriorityQueue
N = int(input())
plusPq = PriorityQueue()
minusPq = PriorityQueue()
one = 9
zero = 0

for i in range(N):
    data = int(input())
    if data > 1:
        plusPq.put(data * -1)
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        minusPq.put(data)
