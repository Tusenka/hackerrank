def backpack(a, i, w, indexes=None):
    if indexes is None:
        indexes = set()
    else:
        indexes = indexes.copy()
    if i == len(a) - 1:
        if a[i][0]<=w:
            indexes.add(a[i][2])
            return a[i][1], indexes
        else:
            return 0, indexes
    if w <= 0:
        return 0, indexes
    if w < a[i][0]:
        return backpack(a, i + 1, w, indexes)
    skip, skip_indexes=backpack(a, i+1, w, indexes)
    take, take_indexes=backpack(a, i+1,w-a[i][0], indexes)
    take+=a[i][1]
    if skip>take:
        return skip, skip_indexes
    else:
       take_indexes.add(a[i][2])
       return take, take_indexes


if __name__ == '__main__':
    (n, W) = tuple([int(x) for x in input().rstrip().split()])
    a = []
    for i in range(n):
        (wi, pi) = tuple([int(x) for x in input().rstrip().split()])
        a.append((wi, pi, i+1))
    a.sort(key=lambda x: x[1], reverse=True)
    result=backpack(a, 0, W)
    print(len(result[1]), result[0])
    print(*sorted(result[1]))
