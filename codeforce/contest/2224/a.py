def solve(a: list[int]):

    for i in range(len(a)-2, -1, -1):
        if a[i+1]>0:
           a[i]=a[i]+a[i+1]

    return len([1 for x in a if x>0])


t=int(input())

for _ in range(t):
    input()
    a=list(map(int, input().split()))

    print(solve(a))
