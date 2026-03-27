_MAX=10**9

def solve(n: int, k: int):
    if k>n:
       return None

    b = str(bin(n))[2:]

    bits=[0]*len(b)
    count1=0

    for i, x in enumerate(b):
        if x=='1':
           bits[i]+=1
           count1+=1

    if count1>k:
        return None

    rest=k-count1

    while rest:
        for x in range(len(bits)-1):
            if not bits[x]:
                continue

            bits[x]-=1
            rest-=1
            bits[x+1]+=2

            if not rest:
               break

    ans=[]
    for i, c in enumerate(bits):
        if c:
           ans.extend([2**(len(bits)-i-1)]*c)


    return ans


n,k=tuple(map(int, input().split()))

ans=solve(n, k)

if ans:
    print("YES")
    print(*ans)
else:
    print("NO")