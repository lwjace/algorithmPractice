import sys
sys.stdin=open("input.txt", "rt")

T= int(input()) #첫줄에 몇 개의 케이스가 있는지 읽고
for t in range(T): #케이스가 T개 있으니까 T번 반복해서 저장
    n, s, e, k =map(int, input().split()) # 케이스 별 숫자들 읽기
    alist = list(map(int, input().split())) # 케이스 별 리스트 읽기
    a = a[s-1:e]
    alist.sort()
    print( "#%d %d" %(t, a[k-1])) #숫자 출력을 변수로 넣는 방법