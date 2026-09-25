def solve(x,y,k):
    z=y-x
    ans=max(x+k-max(x,z+1), 0)*z
    for i in range(x, min(x+k-1,z)+1):
        ans+=z%i

    return ans


t=int(input())

for _ in range(t):
    x,y,k=tuple(map(int, input().split()))
    print(solve(x,y,k))