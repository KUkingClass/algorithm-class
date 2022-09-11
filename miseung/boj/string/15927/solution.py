import sys, math

if __name__ == "__main__":
    S = sys.stdin.readline().strip()
    l = len(S)
    if S == S[0] * l:
        print(-1)
    elif S[:l // 2][::-1] == S[math.ceil(l / 2):]:
        print(l - 1)
    else:
        print(l)
