n = int(input())

sp = 1
ep = 1
sum = 1 
answer = 1
while ep != n:
    if sum == n:
        answer += 1
        sum -= sp 
        sp += 1 
    elif sum < n:
        ep += 1 
        sum += ep
    else:
        sum -= sp
        sp += 1

print(answer)
        
        