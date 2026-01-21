def solve(s):
    if "YY" in s:
        return "NO"

    count = 0

    for x in s:
        if x == "Y":
            count += 1
        if count > 1:
            return "NO"
    return "YES"


t = int(input())

for _ in range(t):
    s = input().strip()
    print(solve(s))
