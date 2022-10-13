import sys


def get_next_max(cur_position, start, heights):
    min_value = next((x for x in heights[cur_position:] if x > start), 0)
    return min_value if min_value else max(heights[cur_position:])


if __name__ == '__main__':
    h, w = map(int, sys.stdin.readline().split())
    heights = list(map(int, sys.stdin.readline().split()))

    start = heights[0]
    cur_idx = 1
    answer = 0

    while cur_idx < w - 1:
        end = get_next_max(cur_idx, start, heights)
        end_idx = heights.index(end, cur_idx)
        limit = min(start, end)
        for i in range(cur_idx, end_idx):
            answer += max(0, limit - heights[i])
        cur_idx = end_idx + 1
        start = heights[end_idx]

    print(answer)
