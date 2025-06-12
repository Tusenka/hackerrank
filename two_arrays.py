def _check_range(x, _range):
    if _range[1] >= x[1] >= _range[0] or _range[1]>=x[0]>=_range[0]:
        return True
    return _range[1] <= x[1] and x[0] <= _range[0]


def find_range(a: list, x: int):
    _max=x
    _min=x
    for _, x in enumerate(a):
        if _check_range(x, (_min, _max)):
            if x[1]>=_max:
                _max=x[1]
            if x[0]<=_min:
                _min=x[0]
    return _min, _max

def count_permutations(a: list, x: int, m: int):
    ranges=find_ranges(a, x)
    return ranges[1]-ranges[0]+1



if __name__ == '__main__':
    t=int(input().rstrip())
    for t_itr in range(t):
        (n, x, m) = tuple([int(x) for x in input().rstrip().split()])
        a = list([int(x) for x in input().rstrip().split()])
        b = list([int(x) for x in input().rstrip().split()])
        result = count_permutations(a, x, m)
        print(result)
