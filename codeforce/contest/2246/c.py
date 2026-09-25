from functools import cache

M=(10**9)+7

@cache
def fact(n: int):
    if n<=1:
       return 1
    return n*fact(n-1)

def comb2(n: int):
    if n<=2:
        return 1
    return (n-1)*(n-1+1)//2

def solve(a: list[int]):
    s=set(a)
    i=0
    while i < len(a) and a[i]==-1:
        i+=1

    if i:
       c=0
       for i in range(1,len(a)):
           if a[i]==a[i-1]+1:
              c+=1
       return (2**((len(a)-len(s))))*(c+1)
    else:
        return 2**((len(a)-len(s)))

t=int(input())

for _ in range(t):
    input()
    a=list(map(int, input().split()))

    print(solve(a=a))
