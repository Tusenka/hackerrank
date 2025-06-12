boos=[]
def _find_next_max(a, j, sign):
    _max=a[j]
    while j<len(a) and a[j]*sign>0:
        if a[j]>_max:
            _max=a[j]
        j+=1
    if j==len(a)-1 and a[-1]*sign>0:
        return -1, _max
    return j, _max
#[()]
def _find_first(a: list, t:int, i):
    while i<len(a) and a[i]>t:
        i+=1
    if i>=len(a)-1:
        return -1 if a[-1] > t else i
    return i


def _count_books(a: list, t: int):
    _max=1
    t0=t
    i=_find_first(a, t, 0)
    if i==-1: return 0
    if i==len(a)-1: return 1
    j=i+1
    t-=a[i]
    while i<len(a):
        while j<len(a) and t-a[j]>=0:
            t-=a[j]
            j+=1
        if i==j:
            return max(_count_books(a[i+1:], t0), _max)
        #we've already increased j
        if _max<j-i:
            _max=j-i
        t+=a[i]
        i+=1
    return _max



def count_books(a: list, t: int):
    return _count_books(a, t)


if __name__ == '__main__':
    (n, t) = tuple([int(x) for x in input().rstrip().split()])
    a = list([int(x) for x in input().rstrip().split()])
    result = _count_books(a, t)
    print(result)



