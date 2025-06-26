#https://codeforces.com/contest/2120/problem/A
def _solve(a, b, c):

    if a[1]==b[1]==c[1]:
        return a[0]+b[0]+b[0]==c[1]
    if a[0]==b[0]==c[0]:
        return a[1]+b[1]+b[1]==c[0]
    if b[1]+c[1]==a[1] and b[0]==c[0]:
        return b[0]+a[0]==a[1]
    if b[0]+c[0]==a[0] and b[1]==c[1]:
        return b[1]+a[1]==a[0]

    return False

t=int(input())

for _ in range(t):
    l1, b1, l2, b2, l3, b3 = tuple(int(x) for x in input().rstrip().split())
    if _solve((l1, b1), (l2, b2), (l3, b3)):
        print("YES")
    else:
        print("NO")