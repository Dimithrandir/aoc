def solve_part_one(layout):
    new_layout = []
    for i in range(len(layout)):
        new_layout.append([])
        for j in range(len(layout[i])):
            seat = layout[i][j]
            new_layout[i].append('#' if seat == 'L' else '.')

    while layout != new_layout:
        for i in range(len(new_layout)):
            layout[i] = new_layout[i].copy()
        for i in range(len(layout)):
            for j in range(len(layout[i])):
                seat = layout[i][j]
                if seat == '.':
                    new_layout[i][j] = '.'
                    continue
                neighbors = [(x, y)
                             for x in range(i-1, i+2)
                             for y in range(j-1, j+2)
                             if (x, y) != (i, j) and x in range(len(layout)) and y in range(len(layout[i])) and layout[x][y] != '.']
                n_vals = [layout[x[0]][x[1]] for x in neighbors]
                if seat == '#' and n_vals.count('#') >= 4:
                    new_layout[i][j] = 'L'
                if seat == 'L' and n_vals.count('#') == 0:
                    new_layout[i][j] = '#'

    print(len([seat for row in new_layout for seat in row if seat == '#']))


def solve_part_two(layout):
    n = len(layout)
    m = len(layout[0])
    new_layout = []

    for i in range(n):
        new_layout.append([])
        for j in range(m):
            seat = layout[i][j]
            new_layout[i].append('#' if seat == 'L' else '.')

    while layout != new_layout:
        for i in range(n):
            layout[i] = new_layout[i].copy()
        for i in range(n):
            for j in range(m):
                seat = layout[i][j]
                if seat == '.':
                    new_layout[i][j] = '.'
                    continue
                neighbors = [(x, y)
                             for x in range(i-1, i+2)
                             for y in range(j-1, j+2)
                             if (x, y) != (i, j) and x in range(n) and y in range(m)]
                visibles = []
                for ngb in neighbors:
                    dif = (ngb[0] - i, ngb[1] - j)
                    while ngb[0] in range(n) and ngb[1] in range(m) and layout[ngb[0]][ngb[1]] == '.':
                        ngb = (ngb[0] + dif[0], ngb[1] + dif[1])
                    if ngb[0] in range(n) and ngb[1] in range(m) and layout[ngb[0]][ngb[1]] != '.':
                        visibles.append(ngb)
                v_vals = [layout[x[0]][x[1]] for x in visibles]
                if seat == '#' and v_vals.count('#') >= 5:
                    new_layout[i][j] = 'L'
                if seat == 'L' and v_vals.count('#') == 0:
                    new_layout[i][j] = '#'

    print(len([seat for row in new_layout for seat in row if seat == '#']))


if __name__ == '__main__':
    with open('input') as file:
        data = [list(x) for x in file.read().splitlines()]

    solve_part_one(data.copy())
    solve_part_two(data.copy())
