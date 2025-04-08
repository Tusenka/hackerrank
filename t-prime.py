r=10**6
_primes = [2] * (r+1)
def _build_primes():
    global _primes
    _primes[0] = 0
    _primes[1] = 1
    for i in range(2, r+1):
        if _primes[i]==2:
            j = i
            while i * j <= r:
                _primes[i * j]+=1
                j += 1


if __name__ == '__main__':
        _build_primes()
        n=input()
        a = list([int(x) for x in input().rstrip().split()])
        for x in a:
            i=int(x**0.5)
            if i*i==x and _primes[i]:
                print("YES")
            else:
                print("NO")



