def solve(x:list):
    hash={
        4: '322',
        6: '53',
        8: '7222',
        9: '732'
    }
    ans=''
    for i in x:
        if i in hash:
           ans+=hash[i]
        elif i>1:
            ans+=str(i)

    ans="".join(map(str,sorted(map(int, ans),reverse=True)))
    return ans

n=input()
x=list(map(int, input()))
print(solve(x))