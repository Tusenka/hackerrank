from functools import reduce


def get_speed(a: list):
    z0 = 1
    z1 = 1
    for i in range(1, len(a)):
        z0 = z0 * a[i]
        z1 = z1 * a[i - 1]
    return z0 / z1


def swap_and_get_speed(a: list, i: int, j: int, last_speed: int):
    last_speed *= (a[j] * a[0]) / (a[-1] * a[i])
    return last_speed


def solve(a):
    last_speed = get_speed(a)

    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                continue
            if swap_and_get_speed(a, i, j, last_speed) == 1:
                return True

    return False


t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    a = list(map(int, input().rstrip().split()))
    print("YES" if solve(a) else "NO")
