from collections import defaultdict


def solve(s):
    hash = defaultdict(int)
    for ch in s:
        hash[ch] += 1
    odd = set(ch for ch in s if hash[ch] % 2)
    even = set(ch for ch in s if hash[ch] % 2 == 0)
    for step in range(len(s)):
        if len(odd) == 0 or len(odd) == 1:
            return "First" if step % 2 else "Second"
        if even:
            ch = even.pop()
            hash[ch] -= 1
            odd.add(ch)


s = input()
print(solve(s))
