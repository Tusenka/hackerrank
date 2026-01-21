# https://codeforces.com/contest/2148/problem/C

t = int(input().rstrip())

for _ in range(t):
    n, m = tuple(map(int, input().rstrip().split()))
    count = 0
    last = 0
    j = 0
    for _ in range(n):
        i, s = tuple(map(int, input().rstrip().split()))
        diff = i - j

        if last != s and diff % 2 == 1:
            count += diff
        elif last == s and diff % 2 == 0:
            count += diff
        else:
            count += diff - 1
        last = s
        j = i
    count += m - j
    print(count)
