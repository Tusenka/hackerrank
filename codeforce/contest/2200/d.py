def solve(a: list[int], x: int, y: int):
    res=[]
    first=[]
    midle=[]
    end=[]

    iminin=x
    for i in range(x+1, y):
        if a[i]<a[iminin]:
           a[iminin]=i

    shift_in_array(a=a, i=x, j=y, sh=iminin - x)

    for i in range(x+1, y):
        if a[i]<a[iminin]:
            a[iminin]=i

    shift_in_array(a=a, i=x, j=y, sh=iminin - x)


    return res

#shift in place to left
def shift_in_array(a: list, i, j, sh) :
    for _ in range(sh):
        last=a[i]
        for x in range(j-1, i-1, -1):
            a[x]=a[x+1]
        a[j]=last

#shift in place to left
def shift_out_array(a: list, i:int, j:int, sh) :
    for _ in range(sh):
        last=a[-1]
        for x in range(0, len(a), +1):
            if i<=x<=j:
                continue
            a[x]=a[x+1]
        a[-1]=last


t=int(input())

for _ in range(t):
    n,x,y=tuple(map(int, input().split()))
    a=list(map(int, input().split()))

    print(*solve(a=a, x=x, y=y))