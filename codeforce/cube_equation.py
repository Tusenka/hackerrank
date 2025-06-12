import os

def _binary_search(n:int, f: callable):
    r=n
    l=-n
    _try=0
    while f(r)!=0 and _try<100000 and f(l)!=0:
        mid=(r+l)//2
        if f(mid)*f(r)>=0:
            r=mid
        else:
            l=mid
        _try+=1
    if f(r)==0:
        return r
    if f(l)==0:
        return l
    return None


def cube_equation(a, b, c, d):
    return _binary_search(abs(d), lambda x: a*x**3+b*x**2+c*x+d)


f=open("test.txt")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'] if "OUPTUT_PATH" in os.environ else "test_result.log", 'w')

    (a, b, c, d )= tuple([int(x) for x in f.readline().rstrip().split()])

    result=cube_equation(a, b, c, d)

    print(result)

    fptr.write(str(result) + '\n')