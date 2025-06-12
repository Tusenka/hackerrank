def _find_numbers(x:int, m:int):
    p=m-m%x
    ans=p//x - (x<p)
    if 1<=p^x<=m:
        ans+=1
    p+=x
    if 1<=p^x<=m:
        ans+=1

    for y in range(1, min(x-1,m)+1):
        if (x^y) % y==0:
            ans+=1

    return ans

if __name__ == '__main__':
    n = int(input().rstrip())
    for t_itr in range(n):
        (x, m) = tuple([int(x) for x in input().rstrip().split()])
        print(_find_numbers(x, m))




