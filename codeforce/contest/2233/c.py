def solve():
    pass
def maxLength(s):

    n = len(s)
    dp = [0] * n
    maxLen = 0

    for i in range(1, n):

        if s[i] == ')':

            # Check if the previous character is an opening
            # parenthesis '('
            if s[i - 1] == '(':
                if i >= 2:
                    dp[i] = dp[i - 2] + 2
                else:
                    dp[i] = 2

            # Check if the previous character is a
            # closing parenthesis ')' and the matching opening
            # parenthesis exists before the valid substring
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                if i - dp[i - 1] >= 2:
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                else:
                    dp[i] = dp[i - 1] + 2

            # Update the maximum length
            maxLen = max(maxLen, dp[i])

    return maxLen


if __name__ == "__main__":

    s = "(()())"
    print(maxLength(s))