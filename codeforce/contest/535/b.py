
def solve(n: int):
    k=max(map(int, str(n)))
    ans=[0]*k
    for i in range(k):
        sn=sum((1 if x else 0)*(10**j) for j,x in enumerate(reversed(str(n))))
        ans[i]=sn
        n-=sn

    return ans

n=int(input())

ans=solve(n)
print(len(ans))
print(*ans)