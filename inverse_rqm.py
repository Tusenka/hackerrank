from math import log2;


M=10**10
# Enter your code here. Read input from STDIN. Print output to STDOUT
class IncorrectSegmentTree(Exception):
    pass

# TBD
def _get_count_leafs(a: list[int])->int:
    return 2**log2(len(a)+1)-1
 
def _set_leaf_value(a: dict[int, int], s: list[int], res, i: int):
    if res[i]!=M: 
        return res[i]
    if len(s)==0:
        raise IncorrectSegmentTree("Incorrect Segment")
    value=s.pop(0)
    a[value]-=1
    res[i]=value
    return value
    
    
    
def _set_node_value(a: dict[int, int], s:list[int], res:list[int], i:int) -> int:
    if res[i]!=M: 
        return res[i]
    lvalue=_set_value(a, s, res, 2*i+1)
    rvalue=_set_value(a, s, res, 2*i+2)
    if rvalue==M or lvalue==M:
        raise IncorrectSegmentTree("Incorrect Segment")
    value=min(lvalue, rvalue)
    if a[value]==0:
        raise IncorrectSegmentTree("Incorrect Segment")
    a[value]-=1
    res[i]=value
    return value
    
 
def _set_value(a: dict[int, int], s: list[int], res: list[int], i: int):
    if len(res)-1< 2*i+2:
       return _set_leaf_value(a, s,  res,  i)
    else:
       return _set_node_value(a, s, res, i)       
           
        
def solve(a: list[int]):
    possible_leafs=sorted(list(set(a)))
    values={}
    for x in a:
        values[x]=values.get(x, 0)+1
    k=len(possible_leafs)
    res=[M]*len(a)
    if _get_count_leafs(a)>k and False: #TBD
        print('NO')
        return
    else:
        try:
            _set_value(values, possible_leafs, res, 0)
            print('YES')
            print(' '.join([str(x) for x in res]))
        except IncorrectSegmentTree:
            print('NO')
            return
        
    

if __name__ == '__main__':
    n = int(input().strip())

    a = [int(x) for x in input().rstrip().split()]
    
    solve(a)
