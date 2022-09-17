import sys

if __name__ == '__main__':
    expression = sys.stdin.readline().strip()
    stack = []

    try:
        for p in expression:
            if p in ["(", "["]:
                stack.append(p)
            elif p == ")":
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(2)
                else:
                    nums = []
                    while True:
                        top = stack.pop()
                        if str(top).isdigit():
                            nums.append(top)
                        elif top == "(":
                            break
                    stack.append(2 * sum(nums))
            elif p == "]":
                if stack[-1] == "[":
                    stack.pop()
                    stack.append(3)
                else:
                    nums = []
                    while True:
                        top = stack.pop()
                        if str(top).isdigit():
                            nums.append(top)
                        elif top == "[":
                            break
                    stack.append(3 * sum(nums))

        print(sum(stack))
    except:
        print(0)
