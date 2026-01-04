def solve(a):
    i,j=0,1
    ans=0
    while j<len(a)-1:
        if a[j]<=0:
           if a[i]>0 and all([a[x]<0 and a[x]<a[j] for x in range(j+1, len(a))]):
               ans+=a[i]
               i=j
               j+=1
               continue

           ans-=a[j]
           j+=1
           continue
        if a[i]>=0:
            ans+=a[i]
            j+=1
            i=j-1
            continue

        if sum([a[x] for x in range(j, len(a)) if a[x]>=0])>=abs(a[i]):
            ans+=a[i]
            i=j
            j+=1
        else:
            ans-=a[j]
            j+=1

    if a[i]>-a[j]:
        ans+=a[i]
    else:
        ans-=a[j]

    return ans


t=int(input())

for _ in range(t):
    input()
    s=tuple(map(int,input().strip().split()))
    print(solve(s))