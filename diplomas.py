from math import ceil


def _binary_search(n: int, f: callable) -> int:
    r=n
    l=-1
    while r-l>1:
        mid=(r+l)//2
        if f(mid):
            r=mid
        else:
            l=mid

    return r

def find_h(n: int, h: int, w:int) -> int:
    ans=_binary_search(n, lambda k: ceil(n/k)*w<=k*h)
    return min(ans*h, ceil(n/(ans-1))*w)

f=open("test.txt")

if __name__ == '__main__':
    first_multiple_input = f.readline().rstrip().split()

    w = int(first_multiple_input[0])

    h = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = find_h(n, h, w)

    print(result)