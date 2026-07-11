from copy import deepcopy


def solve(a: list[int]):
    if a[-1]==0:
        r=len(a)-1
        while r>=0 and a[r]==0:
            r-=1
    else:
        r=len(a)

    if r==-1:
       del a[:]
       return

    i=0
    j=0
    while i<len(a) and j<len(a):
        while i<r and a[i]!=0:
            i+=1

        if i==r:
           break

        j=max(j, i+1)

        while j<r and a[j]==0:
            j+=1

        while i<r and j<r and a[i]==0 and a[j]!=0:
            a[i]=a[j]
            a[j]=0
            i+=1
            j+=1

    del a[i:]

a=list(map(int, input().split()))

solve(a)
print(a)

