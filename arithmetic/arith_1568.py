a, b, c = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def Execute(a, b):
    ret = [0] * 2
    if b == 0:
        ret[0] =1
        ret[1] =0
        return ret