_visited=set()
def _find_min_cost_fuel(a: list, k: int):
    i=0
    _sum=0
    c=0
    while i < len(a) - 1:
        j = i + 1
        while j <= min(i + k - 1, len(a) - 2) and a[j] >= a[i]:
                j += 1
        if c < (j - i):
            _sum += a[j] * (j - i - c)
            c += j - i
        c-=j-i
        i = j
    return _sum



if __name__ == '__main__':
    (n, k) = tuple([int(x) for x in input().rstrip().split()])
    a = list([int(x) for x in input().rstrip().split()])
    result = _find_min_cost_fuel(a, k)
    print(result)



