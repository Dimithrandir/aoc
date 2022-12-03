def get_line(points):
    line = []
    if points[0][0] == points[1][0]:
        if points[0][1] < points[1][1]:
            line = [(points[0][0], x) for x in range(points[0][1], points[1][1] + 1)]
        else:
            line = [(points[0][0], x) for x in range(points[0][1], points[1][1] - 1, -1)]
    elif points[0][1] == points[1][1]:
        if points[0][0] < points[1][0]:
            line = [(x, points[0][1]) for x in range(points[0][0], points[1][0] + 1)]
        else:
            line = [(x, points[0][1]) for x in range(points[0][0], points[1][0] - 1, -1)]
    else:
        # part two solution
        x1 = points[0][0]
        y1 = points[0][1]
        x2 = points[1][0]
        y2 = points[1][1]
        i = x1
        j = y1
        if x1 < x2 and y1 < y2:
            for k in range(x1, x2 + 1):
                line.append((i, j))
                i += 1
                j += 1
        elif x1 > x2 and y1 < y2:
            for k in range(x2, x1 + 1):
                line.append((i, j))
                i -= 1
                j += 1
        elif x1 > x2 and y1 > y2:
            for k in range(x2, x1 + 1):
                line.append((i, j))
                i -= 1
                j -= 1
        elif x1 < x2 and y1 > y2:
            for k in range(x1, x2 + 1):
                line.append((i, j))
                i += 1
                j -= 1
    return line

def get_overlaps(lines):
    overlaps = 0
    dic = {}
    pairs = [coord for line in lines for coord in line]

    for pair in pairs:
        if pair not in dic:
            dic[pair] = 1
        else:
            dic[pair] += 1

    for value in dic.values():
        if value > 1:
            overlaps += 1
    
    return overlaps

def solve_part_one(coords):
    lines = []
    for coord in coords:
        line = get_line(coord)
        if line:
            lines.append(line)
    print(get_overlaps(lines))

if __name__ == '__main__':
    with open('input') as file:
        data = file.read().splitlines()
        coords = []
        for row in data:
            coords.append([list(map(int, row.split(' ')[0].split(','))),
                           list(map(int, row.split(' ')[2].split(',')))])

    solve_part_one(coords)
