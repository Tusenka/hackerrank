import os

def twoSubsequences(x, r, s):
    if r-s < 0 or (r + s) % 2 != 0 or (r - s) % 2 != 0 or r == 0:
        return 0
    m = len(x)
    MOD = (10 ** 9) + 7
    h, l = (r + s) // 2, (r - s) // 2
    result = 0
    dp = [[ 0 for i in range(m + 1) ] for j in range(h + 1)]
    dp[0][0] = 1
    for i in range(0, m):
        for j in range(h, 0, -1):
            for k in range(1, m + 1):
                if j >= x[i]:
                    dp[j][k] = (dp[j - x[i]][k - 1] + dp[j][k]) % MOD
    for i in range(m):
        result = (result + (dp[h][i] * dp[l][i])) % MOD
    return result

f=open("test.txt")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = f.readline().rstrip().split()

    m = int(first_multiple_input[0])

    r = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    x = list(map(int, f.readline().rstrip().split()))

    result = twoSubsequences(x, r, s)

    fptr.write(str(result) + '\n')