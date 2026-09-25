def gcd(x, y):
    if x>y:
       y,x=y,x
    while y%x:
        x=y%x
    return x

def solve(a:list[int]):
    return gcd(a[0], a[-1])

t=int(input())
for _ in range(t):
    input()
    a=list(map(int, input().split()))
    print(solve(a=a))