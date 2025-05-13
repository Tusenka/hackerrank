import random

def _get_median(a:tuple):
    return findMedian(list(a))


def partition(arr, l, r):
    lst = arr[r]
    i = l
    j = l
    while j < r:
        if arr[j] < lst:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def _random_partition(arr, l, r):
    n = r - l + 1
    pivot = random.randint(0, n - 1)
    i = l + pivot
    arr[i], arr[r] = arr[r], arr[i]
    return partition(arr, l, r)

def _median_utils(arr, l, r, k, a, b):
    if l <= r:
        partitionIndex = _random_partition(arr, l, r)
        # find the median of odd number element in arr[]
        if partitionIndex == k:
            b[0] = arr[partitionIndex]
            if a[0] != -1:
                return
        elif partitionIndex == k - 1:  # a & b as middle element of arr[]
            a[0] = arr[partitionIndex]
            if b[0] != -1:
                return
        # index in first half of the arr[]
        if partitionIndex >= k:
            _median_utils(arr, l, partitionIndex - 1, k, a, b)

        # find the index in second half of the arr[]
        else:
            _median_utils(arr, partitionIndex + 1, r, k, a, b)

def findMedian(arr):
    a = [-1]
    b = [-1]
    n = len(arr)
    _median_utils(arr, 0, n - 1, n // 2, a, b)
    return b[0]

def _iterate(n):
    x = 2 ** (n)
    for s in range(x):
        s = str(bin(s))[2:]
        s = s.zfill(n)
        yield s


def _eval_median(a:tuple, x: int, i=0, j=None):
    m=_get_median(a)
    if abs(m)==abs(x):
        return "YES"
    for i in _iterate(len(a)):
        a0=tuple([a[j] if i[j]=='0' else -a[j] for j in range(len(a))])
        m=_get_median(a0)
        if abs(m)==abs(x):
            return "YES"
    return "NO"


def _eval(a, x=None):
    x=a[0]
    return _eval_median(a, x)

t=int(input().rstrip())
for t_itr in range(t):
    (n) = tuple([int(x) for x in input().rstrip().split()])
    a = list([int(x) for x in input().rstrip().split()])
    print(_eval(a))