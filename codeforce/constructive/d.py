def solve(n:int, k:int, s:int):
    if k>s or s>(n-1)*k:
        return []

    rest=[1]*k

    x=s-k
    for i in range(k):
        v=min(n-2, x)
        x-=v
        rest[i]+=v

    res=[0]*k
    for i in range(k):
        if i%2:
           res[i]=res[i-1]-rest[i]
        else:
          res[i]=(res[i-1] if i>0 else 1)+rest[i]

    return res

n,k,s=tuple(map(int, input().split()))
ans=solve(n=n, k=k, s=s)

print("YES" if ans else "NO")

if ans:
   print(*ans)