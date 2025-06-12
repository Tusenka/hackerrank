import functools

@functools.cache
def _count_permutation(n: int):
    if n==3:
        return 1
    elif n<3:
        return 0
    if n%2==0:
        return _count_permutation(n>>1) << 1
    else:
        return _count_permutation((n>>1))+_count_permutation((n>>1)+1)


if __name__ == '__main__':
    n = int(input().rstrip())
    result = _count_permutation(n)
    print(result)



