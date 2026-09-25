def solve(k, a):
    n=len(a)

    h={x: 0 for x in a}
    for x in a:
        h[x]+=1

    hr={x: 0 for x in range(max(h.values())+1)}
    for x in h.values():
        hr[x]+=1

    count=0
    for x in hr.keys():
        r=0
        d=0
        for i in h.values():
            if i>x:
                r+=1
            else:
                d+=i
        if r==0:
            continue

        v=n-d-x*r
        if v>k or (k-v)%r:
           continue

        if x<len(hr.keys()) and not hr[x+1]:
            continue

        count+=1

    return count



t=int(input())

for _ in range(t):
    n,k=tuple(map(int, input().split()))
    a=list(map(int, input().split()))
    print(solve(k, a))