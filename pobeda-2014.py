import os

def _binary_search(n:int, f: callable):
    r=n
    l=-1
    while r-l>1:
        mid=(r+l)//2
        if (f(mid)):
            l=mid
        else:
            r=mid
    if f(r):
        return r
    return l

def build_monitor(a: tuple):
    _count=min(a[0], a[1])+ min(a[2], a[3])
    return _binary_search (_count//2, lambda i: i*i<=_count)

f=open("test.txt")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'] if "OUPTUT_PATH" in os.environ else "test_result.log", 'w')

    a= tuple([int(x) for x in f.readline().rstrip().split()])

    result=build_monitor(a)

    print(result)

    fptr.write(str(result) + '\n')