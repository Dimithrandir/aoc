pipes = {'T': '7|F', 'B': 'J|L', 'L': 'L-F', 'R': 'J-7'}
coords = {'T': (-1, 0), 'B': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def get_neighboring_pipes(pipe, tiles):
    tile = tiles[pipe[0]][pipe[1]]
    directions = ([x for x in pipes.keys() if tile in pipes[x]]
                  if tile in '-|'
                  else [x for x in pipes.keys() if tile not in pipes[x]])
    return [(pipe[0] + coords[x][0], pipe[1] + coords[x][1])
            for x in directions
            if pipe[0] + coords[x][0] in range(len(tiles))
            and pipe[1] + coords[x][1] in range(len(tiles[0]))
            and tiles[pipe[0] + coords[x][0]][pipe[1] + coords[x][1]] in pipes[x]]


def solve_part_one(tiles):
    prev_pipes = [(''.join(tiles).index('S') // len(tiles[0]), ''.join(tiles).index('S') % len(tiles[0]))]
    curr_pipes = [y for x in prev_pipes for y in get_neighboring_pipes(x, tiles)]
    distance = 1
    while len(set(curr_pipes)) > 1:
        next_pipes = [y for x in curr_pipes for y in get_neighboring_pipes(x, tiles) if y not in prev_pipes]
        prev_pipes = curr_pipes
        curr_pipes = next_pipes
        distance += 1

    print(distance)


def solve_part_two(tiles):
    prev_pipes = [(''.join(tiles).index('S') // len(tiles[0]), ''.join(tiles).index('S') % len(tiles[0]))]
    curr_pipes = [y for x in prev_pipes for y in get_neighboring_pipes(x, tiles)]
    loop = curr_pipes.copy()
    loop.insert(1, prev_pipes[0])
    while len(set(curr_pipes)) > 1:
        next_pipes = [y for x in curr_pipes for y in get_neighboring_pipes(x, tiles) if y not in prev_pipes]
        prev_pipes = curr_pipes
        curr_pipes = next_pipes
        loop.insert(0, curr_pipes[0])
        loop.append(curr_pipes[1])

    loop = list(reversed(loop[:-1]))
    count = 0
    for i, row in enumerate(tiles):
        loop_part = sorted(set(loop).intersection([(i, j) for j in range(len(row))]), key=lambda l: l[1])
        ins = [x for x in loop_part if loop[(loop.index(x) + len(loop) - 1) % len(loop)][0] > x[0]]
        outs = [x for x in loop_part if loop[(loop.index(x) + 1) % len(loop)][0] > x[0]]
        for k, (_, j) in enumerate(ins):
            count += len([x for x in [(i, y) for y in range(len(row))] if x[1] in range(j, outs[k][1]) and x not in loop_part])

    print(count)


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
