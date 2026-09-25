from math import sqrt

def build_primes(n):
    primes=[True]*(n+1)

    for i in range(2, n):
        if not primes[i]:
            continue
        j=2
        while j*i<=n:
            primes[j*i]=False
            j+=1
    return {i for i in range(n) if primes[i]}



def solve(n: int):
    primes=build_primes(int(sqrt(n)))
    primes.remove(1)
    primes.remove(0)
    if n<=3:
       return [n, 0]
    c=0
    fact=[0]*(max(primes)+1)
    for i in primes:
        if not n%i:
           fact[i]+=1
    for i, x in enumerate(fact):
        while x and not x%2:
            x=x/2
        while x>1:
           x+=1
           while x and not x%2:
               x=x//2
           n=n*i
           c=1
           print(x)
        if x==1:
           n=n*i
           c=1

    while sqrt(n)==int(sqrt(n)):
        n=int(sqrt(n))
        c+=1
        if  n==1:
            break
    return [int(n), c]

n=int(input())
print(*solve(n))