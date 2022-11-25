idx = 0


def dfs(cur, target):
    global idx
    if cur == target:
        return idx
    idx += 1

    if len(cur) == 5:
        return
    for ch in ["A", "E", "I", "O", "U"]:
        cur += ch
        if dfs(cur, target):
            return idx
        cur = cur[:-1]


def solution(word):
    return dfs("", word)


if __name__ == '__main__':
    print(solution("AAAAE"))
