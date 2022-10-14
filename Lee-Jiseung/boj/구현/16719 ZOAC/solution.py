str = input()
flags = [False] * len(str)

def choose(left, right):
    if left >= right:
        return

    mn = min(str[left:right]) # [left, right)
    min_index = str[left:right].index(mn) + left
    flags[min_index] = True

    for i, flag in enumerate(flags):
        if flag:
            print(str[i], end='')
    print()

    choose(min_index+1, right)
    choose(left, min_index)

choose(0, len(str))