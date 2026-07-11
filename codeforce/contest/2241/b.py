def solve(x:int):
    return 10**(len(str(x)))+1



t=int(input())

for _ in range(t):
    x=int(input())
    print(solve(x))