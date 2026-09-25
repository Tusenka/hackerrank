def build_primes_and_hashes(m: int):
    hash_=[[] for _ in range(m+1)]
    primes=[]

    for i in range(m+1):
        if hash_[i]:
           continue
        primes.append(i)

        for j in range(m//i):
            hash_[i*j].append(i)

    return hash_, primes

def solve(a: list[int]):
    n=max(max(a), len(a))

    hash_, primes=build_primes_and_hashes(n)
    dp={
        primes[i]:0 for i in range(len(primes))
    }
    for
        for j in hash_[x]:
            dp[j]+=1

    ans=1
    for x in dp:
        ans*=x



t=int(input())

a=list(map(int, input().split()))

