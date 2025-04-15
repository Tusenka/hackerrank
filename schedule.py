_dp=[]
def sweets(sw: list, a: int):
    sw.sort( key=lambda x: x[1]-x[0], reverse=True)
    _counter=0
    for x in sw:
        if a-x[0]>=x[1]:
           a-=x[0]
           _counter+=1
    return _counter

if __name__ == '__main__':
    _ = tuple([int(x) for x in input().rstrip().split()])
    loose = []
    profit = []
    a = list([int(x) for x in input().rstrip().split()])
    b = list([int(x) for x in input().rstrip().split()])
    x=[ x for x in zip(a,b) if x[0]<=x[1] ]
    print(sweets(x, 0))



