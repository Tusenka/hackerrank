import heapq
from heapq import heappush

_dp=[]
def count_profit(a, profit, loose):
    profit.sort( key = lambda x: x[0] )
    i=0
    friends=[]
    while i<len(profit) and profit[i][0]<=a:
        a+=profit[i][1]
        friends.append(profit[i][2])
        i+=1

    loose.sort( key = lambda x: x[1]+x[0], reverse=True )
    loose_auth_friends=[]
    pos=len(friends)
    for x in loose:
        if x[0]<=a:
            heappush(loose_auth_friends, (x[1], pos))
            a+=x[1]
            friends.append(x[2])
            pos+=1
        elif loose_auth_friends:
            last=loose_auth_friends[0]
            if last[0]<x[1]:
                a+=x[1]
                a-=last[0]
                friends[last[1]]=x[2]
                heapq.heapreplace(loose_auth_friends, (x[1], last[1]))

    return friends


if __name__ == '__main__':
    (n, x) = tuple([int(x) for x in input().rstrip().split()])
    loose = []
    profit = []
    for i in range(n):
        (a, b) = tuple([int(x) for x in input().rstrip().split()])
        if b>=0:
            profit.append((a, b, i + 1))
        else:
            loose.append((a,b, i + 1))
    result = count_profit(x, profit, loose)
    print(len(result))
    print(*result)



