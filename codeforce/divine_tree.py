#https://codeforces.com/contest/2120/problem/C

def partition(lista,bins):
    if len(lista)==1 or bins==1:
        yield [lista]

    elif len(lista)>1 and bins>1:
        for i in range(1,len(lista)):
            for part in partition(lista[i:],bins-1):
                if len([lista[:i]]+part)==bins:
                    yield [lista[:i]]+part

def _solve(m, n):
    pass

t=int(input())

for _ in range(t):
    n, m = tuple(int(x) for x in input().rstrip().split())
    buckets=list(range(3, 5))
    buckets.extend([-1]*(5))
    for x in partition(buckets, 5 ):
        print(x)


