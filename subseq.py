MOD=998244353
def _find_range(a: list, b:list):
    if len(b)==1:
        return int(b[0]==min(a))
    for x in range(len(a)-1, len(a)-len(b)-2, -1):
        if a[x]<b[-1]:
            return 0
        if b[-1]==a[x]:
            j=x
            break
    else:
        return 0
    bi=len(b)-1
    count=0
    mult=1
    while j>=0 and bi>0:
        if a[j]<b[bi]:
            mult=count*mult
            count=0
            bi-=1
            while j>=0:
                if a[j]<b[bi]:
                    return 0
                if a[j]==b[bi]:
                    break
                j-=1
            else:
                return 0
        j-=1
        count+=1
    mult=mult*count
    if bi>1:
        return 0
    if min(a[:j+2])==b[0]:
        return mult % MOD
    else:
        return 0

def count_permutations(a: list, b:list):
    return _find_range(a, b)



if __name__ == '__main__':
    (n, m) = tuple([int(x) for x in input().rstrip().split()])
    a = list([int(x) for x in input().rstrip().split()])
    b = list([int(x) for x in input().rstrip().split()])
    result = count_permutations(a, b)
    print(result)





