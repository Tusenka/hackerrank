def fib(n, fib1, fib2, i):
    if i==n:
        return fib2+fib1
    return fib(n, fib2, fib1+fib2, i+1)


if __name__ == '__main__':
    n=int(input())
    print(fib(n, 1, 1, 2))
