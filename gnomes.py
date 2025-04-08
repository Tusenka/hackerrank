def solve(a: list):
    a.sort(key=lambda x: x[0]+x[1], reverse=True)
    bi=a[0][1]
    for x in a[1:]:
      bi-=x[0]
      if bi>x[1]:
         bi=x[1]
    return [x[2] for x in a] if bi>0 else [-1]


if __name__ == '__main__':
    n = int(input().rstrip())
    a=[]
    for t_itr in range(n):
        (ai, bi) = tuple([int(x) for x in input().rstrip().split()])
        a.append((ai, bi, len(a)+1))
    print(*solve(a))




