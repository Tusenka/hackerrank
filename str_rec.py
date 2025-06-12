def str_perm(s, i, s1):
    if i == len(s):
        print(s1)
        return
    str_perm(s, i + 1, s1)
    str_perm(s, i + 1, s1 + s[i])


if __name__ == '__main__':
    s = str(input())
    str_perm(s, 0, "")
