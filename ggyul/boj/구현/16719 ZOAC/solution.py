'''
https://www.acmicpc.net/problem/16719
ZOAC
'''

word = input()
n = len(word)
visited = [False] * n

def go(index):
    while True:
        if all(visited[i] for i in range(index, n)):
            return
        next = -1
        for i in range(index, n):
            if not visited[i]:
                if next == -1:
                    next = i
                elif word[next] > word[i]:
                    next = i
        if next != -1:
            visited[next] = True
            for i in range(len(visited)):
                if visited[i]:
                    print(word[i], end='')
            print()
            go(next)
        
go(0)