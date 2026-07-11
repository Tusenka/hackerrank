# https://codeforces.com/contest/2183/problem/A
def build_prefix(a: list):
    ans = [0] * len(a)
    ans[0] = a[0]
    for i in range(1, len(a)):
        ans[i] += ans[i - 1] + a[i]

    return ans


def get_sum(prefix, i, j):
    return prefix[j] - prefix[i]


def solve(a: list):
    step = 1
    prefixes = build_prefix(a)
    while len(a) > 1:
        if step == 1:
            for i in range(len(a) - 1):
                for j in range(i + 1, len(a)):
                    if get_sum(prefixes, i, j) == j - i:
                        a[j] = 0
                        del a[i:j]
                        break
                break

            else:
                del a[0]
                a[0] = 1

        else:
            for i in range(len(a) - 1):
                for j in range(i + 1, len(a)):
                    if get_sum(prefixes, i, j) <= j - i:
                        a[j] = 1
                        del a[i:j]
                        break
                else:
                    continue
                break

            else:
                del a[0]
                a[0] = 0

        prefixes = build_prefix(a)
        step *= -1

    return a[0]


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print("BOB" if solve(a) else "ALICE")
