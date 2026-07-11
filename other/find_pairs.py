shared_counter=[1, 1, 2, 3, 5, 8, 13, 21]
def fibonacci(n):
    """Yield the first n Fibonacci numbers."""
    if len(shared_counter)>n:
        for i in range(len(shared_counter)):
            yield shared_counter[i]
        return

    for x in fibonacci(n-1):
        yield x

    shared_counter.append(shared_counter[n-1]+shared_counter[n-2])
    yield shared_counter[n]