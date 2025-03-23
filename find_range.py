

def _build_commands(a: list):
    a.sort()
    l=0
    _max=0
    for r in range(1, len(a)):
        while a[r]-a[l]>5:
            l+=1
        if r-l+1>_max:
           _max=r-l+1
    return _max


if __name__ == '__main__':
        n=input().rstrip()
        a = list([int(x) for x in input().rstrip().split()])

        result = _build_commands(a)

        print(result)