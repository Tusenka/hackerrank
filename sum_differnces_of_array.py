def sum_diff_of_given_array(a: list[int]) ->list[int]:
    _sum=0
    a=sorted(a)
    for i, x in enumerate(a):
        _sum+=i*x-(len(a)-i-1)*x
    return _sum

if __name__ == '__main__':
    q = [ int(x) for x in input().strip().split() ]
    print(sum_diff_of_given_array(q))