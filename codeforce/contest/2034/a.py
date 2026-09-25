def gcd(a: int, b: int):
    if b==0:
       return a
    if a<b:
        a,b=b,a
    return gcd(b, a % b)

def solve(a: int, b: int):
    if b==a:
       return a

    return (a*b)//gcd(a, b)

t=int(input())

for _ in range(t):
    a,b=tuple(map(int, input().split()))

    print(solve(a=a, b=b))