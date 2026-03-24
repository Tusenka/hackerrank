def solve(a: list[int]):
    odd_sum=sum(a[i] for i in range(0,len(a),2))
    even_sum=sum(a[i] for i in range(1,len(a),2))
    if odd_sum>even_sum:
       return [a[i] if  i%2==0 else 1 for i in range(len(a))]
    else:
       return  [a[i] if  i%2 else 1 for i in range(len(a))]

t=int(input())

for _ in range(t):
    input()
    a=list(map(int, input().split()))
    print(*solve(a))
