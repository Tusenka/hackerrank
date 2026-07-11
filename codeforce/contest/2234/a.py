def solve(a: list[int]):
    a.sort(reverse=True)

    for i in range(1, len(a)-1):
        if a[i+1] != a[i-1] % a[i]:
           return [-1]

    return [a[0], a[1]]


t=int(input())

for _ in range(t):
    input()
    a=list(map(int, input().split()))

    print(
        * solve(a=a))