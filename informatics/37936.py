def solve(a: list[tuple[int, int, int]]):
    events=[]

    for x in a:
         events.append((x[1],0))
         events.append((x[0],1))

    events.sort()
    start=-1
    o=0
    for x in events:
        if not x[1]:
           start=x[0]
           o+=1
        else:
           if not x[1]:
               return 0
           else:
               return x[0] - start








n=int(input())
a=[None]*n

for i in range(n):
   raw=tuple(map(int, input().split()))

   start = raw[0] * 60 * 60 + raw[1] * 60 + raw[2]
   end = raw[3] * 60 * 60 + raw[4] * 60 + raw[5]

   a[i]=(end-start if end>start else 24*60*60 ,start, end if end>start else end+24*60*60)

print(solve(a=a))


