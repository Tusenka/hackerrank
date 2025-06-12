_dp=0
def _find_next_max(a, j, sign):
    _max=a[j]
    while j<len(a) and a[j]*sign>0:
        if a[j]>_max:
            _max=a[j]
        j+=1
    if j==len(a)-1 and a[-1]*sign>0:
        return -1, _max
    return j, _max

def _find_subs(a: list):
    _sum=0
    i=0
    while i<len(a):
        i, _max=_find_next_max(a, i, a[i])
        _sum+=_max
        if i<0:
            break
    return _sum

def count_subs(a: list):
    i=0
    return _find_subs(a)

if __name__ == '__main__':
    t=int(input().rstrip())
    for t_itr in range(t):
        (n) = tuple([int(x) for x in input().rstrip().split()])
        a = list([int(x) for x in input().rstrip().split()])
        result = count_subs(a)
        print(result)



