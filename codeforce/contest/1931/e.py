import heapq

def count_null(v):
    v=str(v)
    ans=0
    for x in reversed(v):
        if x=='0':
           ans+=1
        else:
           break

    return ans



def solve(a:list[int]):
    a=[(count_null(v), len(str(v))-count_null(v)) for v in a]
    a.sort()

    for i in range(len(a)-1, -1, -2):
        a[i]=(0,a[i][1])

    return sum(a[i][1]+a[i][0] for i in range(len(a)))>=m+1

t=int(input())

for _ in range(t):
    n, m = tuple(map(int, input().split()))
    a=list(map(int, input().split()))

    print("Sasha" if solve(a) else "Anna")