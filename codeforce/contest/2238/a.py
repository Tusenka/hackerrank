M=10**9

def solve(a: list[int], b: list[int], c :int):
    sa=sorted(a, reverse=True)
    sb=sorted(b, reverse=True)

    diff=0
    for i, x in enumerate(sb):
        if x>sa[i]:
           return -1
        else:
           diff+=sa[i]-x

    ans=0
    for i,x in enumerate(b):
        if x>a[i]:
           break
        ans+=sa[i]-x
    else:
        if ans<=c+diff:
           return ans
        
    return c+diff

t=int(input())

for _ in range(t):
    n, c= tuple(map(int, input().split()))

    a=list(map(int, input().split()))
    b=list(map(int, input().split()))

    print(solve(a=a, b=b, c=c))
