import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    pokemons = []
    cache = {}

    for i in range(n):
        name = sys.stdin.readline().strip()
        pokemons.append(name)
        cache[name] = i + 1

    for _ in range(m):
        case = sys.stdin.readline().strip()
        if case.isdigit():
            print(pokemons[int(case) - 1])
        else:
            print(cache[case])
