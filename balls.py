_dp={'000': []}
def _set_bit(n, i):
    b=1<<(i-1)*2
    return n | b


def _check(row: str):
    global _dp
    if row in _dp:
        yield from _dp[row]
    _dp[row]=[]
    j=0
    while True:
        while j<len(row) and row[j]=='1':
            j+=1
        if j==len(row) or (j==len(row)-1 and row[j]=='0'):
            return
        for i in range(j, len(row)):
            if row[i]=='1':
                _dp[row].append(i)
                yield i
            j=i


def _check_dead(x:list):
    for i in range(len(x)):
        for jj in _check(x[i]):
            for _ in _check("".join([e[jj] for e in x])):
                return True
    return False


def _push_balls(x:list):
    return not _check_dead(x)


def push_balls(x:list):
    if _push_balls(x):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    t = int(input().rstrip())
    for t_itr in range(t):
        x=[]
        (n, m) = tuple([int(x) for x in input().rstrip().split()])
        for _ in range(n):
            x.append(input().rstrip())
        push_balls(x)




