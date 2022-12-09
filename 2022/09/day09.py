def solve_part_one(motions):

    (hx, hy, tx, ty) = 4 * [0]
    visited = [(tx, ty)]
    for move in motions:
        for m in range(int(move[1])):
            hx += 1 if move[0] == 'R' else -1 if move[0] == 'L' else 0
            hy += 1 if move[0] == 'U' else -1 if move[0] == 'D' else 0
            if abs(hx - tx) > 1 or abs(hy - ty) > 1:
                if hx != tx:
                    tx += 1 if hx - tx > 0 else -1
                if hy != ty:
                    ty += 1 if hy - ty > 0 else -1
                visited.append((tx, ty))

    print(len(set(visited)))

def solve_part_two(motions):

    n_knots = 10
    pos = [ [0, 0] for x in range(n_knots) ]
    visited = [(pos[n_knots-1][0], pos[n_knots-1][1])]
    for move in motions:
        for m in range(int(move[1])):
            pos[0][0] += 1 if move[0] == 'R' else -1 if move[0] == 'L' else 0
            pos[0][1] += 1 if move[0] == 'U' else -1 if move[0] == 'D' else 0
            for i in range(1, n_knots):
                if abs(pos[i-1][0] - pos[i][0]) > 1 or abs(pos[i-1][1] - pos[i][1]) > 1:
                    if pos[i-1][0] != pos[i][0]:
                        pos[i][0] += 1 if pos[i-1][0] - pos[i][0] > 0 else -1
                    if pos[i-1][1] != pos[i][1]:
                        pos[i][1] += 1 if pos[i-1][1] - pos[i][1] > 0 else -1
                    if i == n_knots - 1:
                        visited.append((pos[n_knots-1][0], pos[n_knots-1][1]))

    print(len(set(visited)))

if __name__ == '__main__':
    with open('input') as file:
        data = [ x.split(' ') for x in file.read().splitlines() ]

    solve_part_one(data)
    solve_part_two(data)
