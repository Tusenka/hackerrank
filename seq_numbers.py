def _count(a: list, l: int):
    if len(a)==1:
        return 1
    a.sort()
    i=0
    _counter=0
    while i<len(a):
        x=a[i]
        i+=1
        _counter+=1
        while i<len(a) and a[i] <= x+2*l:
            i+=1
    return _counter

if __name__ == '__main__':
    (l, n) = tuple([int(x) for x in input().rstrip().split()])
    a = list([int(x) for x in input().rstrip().split()])
    result = _count(a, l)
    print(result)



