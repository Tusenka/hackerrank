class Tree:
    arr: list[int] = []

    def load(self, n):
        arr=[0]*n



def tree():
    pass

def solve(s: str):
    m=[(x,i) for i,x in enumerate(map(int, s)) if x!=0]

    m.sort(reverse=True)
    rest=0
    arr=[]

    for x,i in m:

        _ans=0
        for j in range(i,len(m)):
            _ans+=(10**m[j][1])*(m[j][0]-rest)

        arr.append(x)
    return arr


def _to_bin(v):
    pass



n=input()
ans=solve(n)
print(len(ans))
print(*ans)