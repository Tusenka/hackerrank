def schedule(a: list):
    _counter=0
    a.sort(key=lambda x: x[1])
    c=0
    for x in a:
        if c <=x[0]:
           c=x[1]
           _counter+=1
    return _counter

if __name__ == '__main__':
    t = int(input().rstrip())
    a=[]
    for t_itr in range(t):
        (b, e) = tuple([int(x) for x in input().rstrip().split()])
        a.append((b, e))
    print(schedule(a))

