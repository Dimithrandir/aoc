import sys
sys.setrecursionlimit(100000)


directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
slash = {'^': '>', '>': '^', 'v': '<', '<': 'v'}
backslash = {'^': '<', '>': 'v', 'v': '>', '<': '^'}


def next_tile(t, d):
    return (t[0] + directions[d][0], t[1] + directions[d][1])


def beam(tile, direction, grid, vis):
    if tile[0] not in range(len(grid)) or tile[1] not in range(len(grid[0])) or (tile, direction) in vis:
        return vis
    vis.append((tile, direction))
    content = grid[tile[0]][tile[1]]
    if direction in '><' and content == '|':
        beam(next_tile(tile, '^'), '^', grid, vis)
        beam(next_tile(tile, 'v'), 'v', grid, vis)
    elif direction in 'v^' and content == '-':
        beam(next_tile(tile, '>'), '>', grid, vis)
        beam(next_tile(tile, '<'), '<', grid, vis)
    else:
        if content in '\\/':
            direction = slash[direction] if content == '/' else backslash[direction]
        beam(next_tile(tile, direction), direction, grid, vis)


def solve_part_one(grid):
    visited = []
    beam((0, 0), '>', grid, visited)

    print(len(set([x[0] for x in visited])))


def solve_part_two(grid):
    visited = []
    n = len(grid)
    max_energized = 0
    for (i, j) in [(i, j) for i in range(n) for j in range(n) if i in [0, n - 1] or j in [0, n - 1]]:
        if i == j or i + j == n - 1:
            dirs = ''
            dirs += 'v' if i == 0 else '^'
            dirs += '>' if j == 0 else '<'
            for d in dirs:
                beam((i, j), d, grid, visited)
                max_energized = max(max_energized, len(set([x[0] for x in visited])))
                visited = []
        else:
            direction = '>' if j == 0 else '<' if j == n - 1 else 'v' if i == 0 else '^'
            beam((i, j), direction, grid, visited)
            max_energized = max(max_energized, len(set([x[0] for x in visited])))
            visited = []

    print(max_energized)


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
