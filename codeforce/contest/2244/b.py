def solve(a):
    if len(a)==1:
        return  True
    psum=[0]*len(a)
    psum[0]=a[0]
    for i in range(1, len(a)):
        psum[i]=psum[i-1]+a[i]

    for x in range(1, len(a)+1):
        if psum[x-1]<x*(x+1)//2:
           return False

    if a[0]==1 and a[1]==1:
        return False

    return True

t=int(input())

for  _ in range(t):
     n=int(input())

     a=list(map(int, input().split()))

     print("YES" if solve(a) else "NO")
