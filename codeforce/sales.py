#https://codeforces.com/contest/2143/problem/B

def solve(a:list, b:list):
    a.sort(reverse=True)
    b.sort()
    j=0
    i=0
    c=0
    while j<len(b) and i<len(a):
        c+=sum(a[i:i+b[j]-1])
        i+=b[j]
        j+=1

    c+=sum(a[i:])

    return c



t = int(input().rstrip())

for _ in range(t):
    _, _ = tuple(input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    print(solve(a, b))