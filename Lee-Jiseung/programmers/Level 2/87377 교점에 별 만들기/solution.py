def solution(line):
    answer = []
    n = len(line)
    intersections = set()
    for i in range(n):
        for j in range(i+1, n):
            slope = line[i][0]*line[j][1] - line[i][1]*line[j][0]
            if slope == 0:
                continue
            x = line[i][1]*line[j][2] - line[i][2]*line[j][1]
            y = line[i][2]*line[j][0] - line[i][0]*line[j][2]
            if x/slope != x//slope or y/slope != y//slope:
                continue
            intersections.add((x//slope,y//slope))
    
    
    intersections = list(intersections)
    minx = min([x for x, _ in intersections])
    maxx = max([x for x, _ in intersections])
    miny = min([y for _, y in intersections])
    maxy = max([y for _, y in intersections])
    
    grid = [['.' for _ in range(maxx-minx+1)] for _ in range(maxy-miny+1)]
    for x, y in intersections:
        grid[maxy-y][x-minx] = '*'
    
    for g in grid:
        answer.append(''.join(g))
        
    return answer