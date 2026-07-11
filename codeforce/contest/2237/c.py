def solve(a: list[int], k: int):
    assert a

    hash={}

    for x in a:
        if x in hash:
           hash[x]+=1
        else:
           hash[x]=1

    keys=sorted(hash.keys())
    if hash[keys[-1]]%2==0:
       return True

    if len(keys)==1:
        return False

    for i in range(len(keys)-1, 0, -1):
        if hash[keys[i]]%2==0:
            return True

        if (keys[i]-keys[i-1])<=k:
            return True

    return hash[keys[0]]%2==0

t=int(input())

for _ in range(t):
    n,k=tuple(map(int, input().split()))
    a=list(map(int, input().split()))

    print("YES" if solve(a=a, k=k) else "NO")