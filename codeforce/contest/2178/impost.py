def solve(s):
    loc = []
    for i, x in enumerate(s):
        if x == "u":
            loc.append(i)
    if len(loc) == 0:
        return 0

    count = 0
    visited = set()
    for i in loc:
        if i in visited:
            continue

        if i == 0 or i == len(s) - 1:
            count += 1
            continue

        if s[i + 1] == "u":
            count += 1
            visited.add(i + 1)

    # try to make all s
    return count


t = int(input())

for _ in range(t):
    s = input().strip()
    print(solve(s))
