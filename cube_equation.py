
def binary_search(n: int, f:callable):
    r=n
    l=-1
    while r-l>1:
        mid=int((r+l)//2)
        if f(mid):
            r=mid
        else:
            l=mid
    


