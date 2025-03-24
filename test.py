def _build_commands(a: list):
    l=0
    _max=[-1] *len(a)
    _min=[10**9]*len(a)
    _max_range=1
    for r in range(0, len(a)):
        _break = 0
        while True:
            if _max[l] < a[r]:
                _max[l:r + 1] = [a[r]] * (r - l + 1)
                _break+=1
            if _min[l] > a[r]:
                _min[l:r + 1] = [a[r]] * (r - l + 1)
                _break+=1
            if l<r and _break<2:
                l+=1
            else:
                break
        while True:
            if _max[l] < a[r]:
                _max[l] = [a[r]]
            if _min[l] > a[r]:
                _min[l] = a[r]
            if abs(_max[l]-_min[l])<=1 and l>0:
                if r - l + 1 > _max_range:
                    _max_range = r - l+1
                l-=1
            elif l==0 and abs(_max[l]-_min[l])<=1:
                if r - l + 1 > _max_range:
                    _max_range = r - l+1
                break
            else:
                break
    return _max_range


if __name__ == '__main__':
        n=input().rstrip()
        a = list([int(x) for x in input().rstrip().split()])

        result = _build_commands(a)

        print(result)