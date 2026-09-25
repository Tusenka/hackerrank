def solve(n: int):
    ans=[1]*n
    if n==1:
        return ans
    ans[1]=2
    if n==2:
        return ans

    ans[2]=3
    if n==3:
        return ans
    
    for i in range(3, n):
        ans[i]=3*2**(i-2)

    x=sum(ans)
    for i in ans:
        if x%i or i>10**17:
            return [-1]
    return ans


t=int(input())

for _ in range(t):
    n=int(input())

    print(*solve(n))