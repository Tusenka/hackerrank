t=int(input())


def _has_del(k: int, a: int, b: int):
    i,j=a//b, 1
    while i<=k:
        if a%i==0 and b%j==0 and a//i==b//j:
           return True
        i+=1
        j+=1
    return False





for _ in range(t):
    a,b,k=tuple(int(x) for x in input().rstrip().split())
    if a<b:
        a,b=b,a
    if a==b:
        print('1')
    elif a/b<=k and _has_del(k, a, b):
        print('1')
    else:
        print('2')

