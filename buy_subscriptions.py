import collections
def _build_purchases(d:int, a: tuple):
    buy=collections.defaultdict(int)
    for i in range(d):
        buy[a[i]]+=1
    _min=len([1 for _, x in buy.items() if x>0])
    _c=_min
    for i in range(d, len(a)):
        buy[a[i-d]]-=1
        buy[a[i]]+=1
        if buy[a[i-d]]==0:
            _c-=1
        if buy[a[i]]==1:
            _c+=1
        if _c<_min:
            _min=_c
        if _min==1:
            return _min
    return _min


q = int(input().strip())

for q_itr in range(q):
    (n, k, d) = tuple([int(x) for x in input().rstrip().split()])
    a = tuple(input().rstrip().split())

    result = _build_purchases(d, a)
    print(result)