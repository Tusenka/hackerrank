def solve(a: list[int])-> list[tuple[int, int]] | None:
    end=0
    new_end=0
    ans=[]
    for start, xend in enumerate(a):
        if xend>new_end and start<=end:
           new_end=xend
           cur=[start, xend]
        if start>end:
           if new_end<end or new_end==0:
              return None
           end=new_end
           ans.append(cur)

        if end>=len(a)-1:
           return ans
    else:
        return None

m=int(input())

a=[0]*(m+1)
while True:
    s=input()
    val=list(int(x) for x in s.split())
    if val[0]==0 and val[1]==0:
       break
    val[0]=min(max(0, val[0]), m)
    val[1]=min(m, val[1])
    a[val[0]]=max(a[val[0]], val[1])

ans=solve(a)
if not ans:
    print("No solution")

else:
    print(len(ans))
    for x in ans:
        print(x[0], x[1])

