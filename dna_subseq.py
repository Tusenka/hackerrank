def _dna_sub(a: str, b: str, ai:int , bj:int):
    if len(a)==len(b):
        return len(a)*(a==b)
    if len(a)==1:
       return a[0] in b
    if b[-1]==a[-1]:
        return _dna_sub(a[:-1], b[:-1])
    else:
        return _dna_sub(a, b[:-1])


if __name__ == '__main__':
    a = input()
    b = input()
    if _dna_sub(a, b):
        print("YES")
    else:
        print("NO")



