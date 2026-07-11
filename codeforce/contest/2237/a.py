def solve(a:list[int])->int:
    pref=[-1]*len(a)
    pref[0]=0

    for i in range(1, len(a)):
        if a[pref[i-1]]>a[i]:
           pref[i]=i
        else:
           pref[i]=pref[i-1]

    i=pref[-1]
    l=len(a)-1
    h=0
    while i>=0:
       h+=(l-i+1)*a[i]
       l=i-1
       if i==0:
          break
       i=pref[i-1]
       if i==l and i==0:
           h+=a[0]
           break

    return h






t=int(input())

for _ in range(t):
    input()
    a=list(map(int, input().split()))

    print(solve(a))