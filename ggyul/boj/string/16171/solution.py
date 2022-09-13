# https://www.acmicpc.net/problem/16171
# 나는 친구가 적다 (Small)
# 6M

word_with_num = input()
key = input()
word=''
for w in word_with_num:
    if w.isalpha():
        word+=w
print(1 if key in word else 0)