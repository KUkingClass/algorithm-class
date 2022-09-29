import sys


def rotated_right(list_2d):
    return [list(elem) for elem in zip(*list_2d[::-1])]


def element_wise_match(board, sticker, start_i, start_j):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j]:
                if not board[start_i + i][start_j + j]:
                    return False

    return True


def find_position(board, sticker, rotated=0):

    if rotated == 4:
        return

    i_max = len(sticker)
    j_max = len(sticker[0])

    if i_max > len(board) or j_max > len(board[0]):
        find_position(board, rotated_right(sticker), rotated + 1)
        return

    for start in range(len(board) - i_max + 1):
        for end in range(len(board[0]) - j_max + 1):
            if element_wise_match(board, sticker, start, end):
                for i in range(i_max):
                    for j in range(j_max):
                        if sticker[i][j]:
                            board[start + i][end + j] = False
                return

    find_position(board, rotated_right(sticker), rotated + 1)


if __name__ == '__main__':
    row, col, k = map(int, sys.stdin.readline().split())
    stickers = [[] for _ in range(k)]

    for i in range(k):
        sticker_r, sticker_c = map(int, sys.stdin.readline().split())
        for _ in range(sticker_r):
            stickers[i].append(list(map(int, sys.stdin.readline().split())))

    board = [[True for _ in range(col)] for _ in range(row)]

    for sticker in stickers:
        find_position(board, sticker)

    print(row*col - sum(map(sum, board)))
