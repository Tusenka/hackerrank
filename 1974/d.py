from mypy.checkpattern import defaultdict

from codeforce.marray import ans


def solve(s: str):
    h=defaultdict(set)

    for i,x in enumerate(s):
        h[x].add(i)

    if abs(len(h['N'])-len(h['S']))%2:
        return 'NO'
    if abs(len(h['E'])-len(h['W']))%2:
        return 'NO'

    ans='R'*len(s)
    dp1={'N': 0, 'W': 0 }
    dp2={'N': 0, 'W': 0 }

    for i,x in enumerate(s):
        match x:
            case 'N':
                if dp1['N']>dp2['N']:
                   dp2['N']+=1
                   ans[i]='R'
                else:
                    dp1['N']+=1
                    ans[i]='H'
            case 'S':
                if dp1['N']>dp2['N']:
                    dp1['N']-=1
                    ans[i]='R'
                else:
                    dp1['N']-=1
                    ans[i]='H'
            case 'W':
                if dp1['W']>dp2['W']:
                    dp2['W']+=1
                    ans[i]='R'
                else:
                    dp1['W']-=1
                    ans[i]='H'
            case 'E':
                if dp1['W']>dp2['W']:
                    dp1['W']-=1
                    ans[i]='R'
                else:
                    dp2['W']-=1
                    ans[i]='H'


t=int(input())

for _ in range(t):
    n=int(input())
    s=input()



