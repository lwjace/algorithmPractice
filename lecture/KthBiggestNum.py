import sys
sys.stdin=open("input.txt", "rt")

n, k = map(int, input().split())
alist = list(map(int, input().split()))
aSet = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            aSet.add(a[i]+a[j]+a[m])

setToList = list(aSet)
setToList.sort(reverse = True)
print(setToList[k-1])