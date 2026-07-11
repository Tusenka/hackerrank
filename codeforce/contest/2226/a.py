M=676767677

def solve(a: list):
    i=0
    _s=0

    while i<len(a):
        _sp=a[i]

        while i<len(a) and (a[i]==1 or (_sp==1 and a[i]==2)):
            _sp=((_sp % M) * (a[i] % M) % M)
            i+=1

        _s=(_s+_sp) % M

        if i==len(a)-1 and a[i]!=1:
            _s+=a[i]
        i+=1

    return _s

t=int(input())

for _ in range(t):
    input()

    a=list(map(int, input().split()))
    print(solve(a=a))