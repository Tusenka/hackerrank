def _ch_sum(y:int):
    return sum(map(int, str(y)))

def solve(x: int):
    _c=0
    for y in range(x, x+300):
        if _ch_sum(y)+x==y:
           _c+=1

    return _c

t=int(input())

for _ in range(t):
    x=int(input())
    print(solve(x))