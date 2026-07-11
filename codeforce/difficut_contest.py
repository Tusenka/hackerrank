t = int(input().rstrip())

for _ in range(t):
    s = input()
    while "FFT" in s or "NTT" in s:
        s = s.replace("FFT", "TFF")
        s = s.replace("NTT", "TTN")
    print(s)
