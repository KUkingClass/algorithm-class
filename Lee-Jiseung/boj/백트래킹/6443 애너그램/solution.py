import sys


def perm(count, flag):
    global word, m, sets, anagram
    if count == m:
        sets[count].add(''.join(anagram))
        return

    for i in range(m):
        if flag & (1<<i):
            continue
        anagram[count] = word[i]
        before = len(sets[count])
        sets[count].add(''.join(anagram[:count+1]))
        if len(sets[count]) > before:
            perm(count+1, flag | (1<<i))


n = int(sys.stdin.readline())
for _ in range(n):
    word = sys.stdin.readline().strip()
    m = len(word)
    sets = [set() for _ in range(m + 1)]
    anagram = [''] * m
    perm(0, 0)
    for s in sorted(sets[m]):
        print(s)
