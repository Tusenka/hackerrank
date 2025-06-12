from functools import cache

M = 10 ** 9 + 7
_fact=[1]*100
def build_fact():
    global _fact
    _fact=[1]*100
    for i in range(1, 100):
        _fact[i]=_fact[i-1]*i

def _get_fact(value: int):
    global _fact

    for i in range (len(_fact)-1, -1, -1):
        if _fact[i]<=value:
            return i
    return -1


@cache
def _build_steps(n: int, last: int):
    if n==0:
        return 0
    if  n>1 and last == 2:
        return 0
    if n == 1:
        return (last>1)
    count = 0
    i=_get_fact(n)
    n0=n-i
    while last-i >= 1 and n0 > 0:
        count+= _build_steps(n0, last=i)
        n0-=1
        i+=1
    if n0==0 and last-i>=1:
        count+=1
    return count


def build_steps(n: int):
    if n==1:
        return 1
    if n==2:
        return 0
    _count=1
    build_fact()
    for i in range(_get_fact(value=n), n):
        _count+=_build_steps(n-i, i)
    return _count


if __name__ == '__main__':
    n = int(input().rstrip())
    print(build_steps(n))
