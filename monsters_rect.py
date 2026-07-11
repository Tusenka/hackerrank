def check_move(i: int, vals: list[list[int]]):
    for j in range(i + 1, len(vals) - (i == -1) - 1):
        if vals[i][0] + 1 < vals[i + 1][0] or (
            vals[i][0] < vals[i + 1][0] and vals[i][1] != vals[i][1]
        ):
            return True
    return False


def get_rect(rows: list[list[int]], cols: list[list[int]]):
    return (rows[-1][0] - rows[0][0] + 1) * (cols[-1][0] - cols[0][0] + 1)


def solve(rows: list[list[int]], cols: list[list[int]]):
    rows.sort()
    cols.sort()

    # minimal element from left=iil1-iil0+abs(jil0-jil1
    idl = (
        (rows[1][0] - rows[0][0], abs(rows[0][1] - rows[1][1]))
        if len(rows) > 1
        else (0, 0)
    )
    # max element from right=iir1-iir0+abs(jir0-jir1)
    idr = (
        (rows[-1][0] - rows[-2][0], abs(rows[-1][1] - rows[-2][1]))
        if len(rows) > 1
        else (0, 0)
    )

    jdu = (
        (cols[1][0] - cols[0][0], abs(cols[0][1] - cols[1][1]))
        if len(cols) > 1
        else (0, 0)
    )
    jdd = (
        (cols[-1][0] - cols[-2][0], abs(cols[-1][1] - cols[-2][1]))
        if len(cols) > 1
        else (0, 0)
    )

    maxes = [idl, idr, jdu, jdd]
    maxes.sort(reverse=True)

    if maxes[0][0] == 0:
        return get_rect(rows=rows, cols=cols)

    for max_ in maxes:
        if max_ == idl and check_move(0, rows) and len(rows) > 1:
            rows[0] = rows[1]
            break

        if max_ == idr and check_move(-1, rows) and len(rows) > 1:
            rows[-1] = rows[-2]
            break

        if max_ == jdu and check_move(0, cols) and len(cols) > 1:
            cols[0] = cols[1]
            break

        if max_ == jdd and check_move(-1, cols) and len(cols) > 1:
            cols[-1] = cols[-2]
            break
    else:
        max_ = maxes[0]

        if max_ == idl and len(rows) > 1:
            rows[0][0] = rows[1][1] - 1
        if max_ == idr and len(rows) > 1:
            rows[-1][0] = rows[-2][0] + 1
        if max_ == jdu and len(cols) > 1:
            cols[0][0] = cols[1][0] - 1
        if max_ == jdd and len(cols) > 1:
            cols[-1][0] = cols[-2][0] + 1

    return get_rect(rows=rows, cols=cols)


t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    rows = []
    cols = []
    for _ in range(n):
        i, j = tuple(map(int, input().rstrip().split()))
        rows.append([i, j])
        cols.append([j, i])
    print(solve(rows=rows, cols=cols))
