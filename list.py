#import sys


#printa = sys.stdout.write
#inputa = sys.stdin.readline

#print(list(map(int, inputa().split())))


import sys 
input = sys.stdin.readline

# 정답 풀이 
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

