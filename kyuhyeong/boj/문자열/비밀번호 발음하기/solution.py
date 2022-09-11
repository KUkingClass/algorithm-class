import sys


def validate_password(password):
    if check_vowel(password) and check_three_successive(password) and check_two_successive(password):
        print("<{}> is acceptable." .format(password))
    else:
        print("<{}> is not acceptable." .format(password))


def check_vowel(password):
    if any(vowel in password for vowel in vowels):
        return True
    return False


def check_three_successive(password):
    if len(password) < 3:
        return True

    for i in range(len(password) - 2):
        window = password[i: i + 3]
        if all(ch in vowels for ch in window) or all(ch in consonants for ch in window):
            return False

    return True


def check_two_successive(password):
    if len(password) < 2:
        return True

    for i in range(len(password) - 1):
        prev, cur = password[i], password[i+1]
        if prev != 'e' and prev != 'o' and prev == cur:
            return False
    return True


if __name__ == '__main__':

    vowels = ["a", "e", "i", "o", "u"]
    consonants = list(set(chr(ch) for ch in range(ord('a'), ord('z') + 1)) - set(vowels))

    while True:
        case = sys.stdin.readline().strip()
        if case == "end":
            break
        validate_password(case)
