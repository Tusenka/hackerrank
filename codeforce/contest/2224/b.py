def solve(a):
    a.sort()

    if a[0]!=0:
       return a[-1]*len(a)



t=int(input())

for _ in range(t):
    input()
    a=list(input())

    print(solve(a))