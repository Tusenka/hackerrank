def fib(n, n1=None):
    if n == 2:
        return 1
    if n == 1:
        return 1
    if n == 0:
        return 0
    last = fib(n - 2)
    if n1 is None:
        n1 = fib(n - 1, last)
    return last + n1
#        если a ≤ 0 или b ≤ 0 или c ≤ 0, то F(a, b, c) = 1#
#        если a > 20 или b > 20 или c > 20, то F(a, b, c) = F(20, 20, 20)
#        если a < b и b < c, то F(a, b, c) = F(a, b, c-1) + F(a, b-1, c-1) - F(a, b-1, c)
#        иначе F(a, b, c) = F(a-1, b, c) + F(a-1, b-1, c) + F(a-1, b, c-1) - F(a-1, b-1, c-1)


if __name__ == '__main__':
    n=int(input())
    print(fib(n, n1=None))
