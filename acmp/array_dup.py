def solve(a: list[int]):
    heap_sort(a=a)
    for i in range(len(a) - 1):
        if a[i] == a[i - 1]:
            return a[i]
    return -1


def heap_sort(a: list):
    def heapify(a: list, n: int, i: int):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and a[l] > a[largest]:
            largest = l

        if r < n and a[r] > a[largest]:
            largest = r

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(a, n, largest)

    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)


a = [3, 0, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print(solve(a=a))
