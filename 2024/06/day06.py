dirs = '^>v<'


def map_area(area, n, cur_dir):
    obstacles = []
    cur_pos = (0, 0)
    for i in range(n):
        for j in range(n):
            if area[i][j] == '#':
                obstacles.append((i, j))
            elif area[i][j] == cur_dir:
                cur_pos = (i, j)
    return obstacles, cur_pos


def solve_part_one(area, loops=False):
    n = len(area)
    cur_dir = '^'
    obstacles, cur_pos = map_area(area, n, cur_dir)
    visited = []

    while cur_pos[0] in range(n) and cur_pos[1] in range(n):
        if loops:
            if not visited:
                visited.append(cur_pos)
            elif visited[-1] != cur_pos:
                visited.append(cur_pos)
                m = len(visited)
                for i in range(m - 1, m // 2 - 1, -1):
                    if visited[2 * i - m:i] == visited[i:]:
                        return -1
        elif cur_pos not in visited:
            visited.append(cur_pos)
        cur_dir_i = dirs.index(cur_dir)
        next_pos = (
                cur_pos[0] + ((cur_dir_i - 1) % (2 if cur_dir_i else -2)),
                cur_pos[1] + (cur_dir_i % (2 if cur_dir_i < 3 else -2)))
        if next_pos in obstacles:
            cur_dir = dirs[(cur_dir_i + 1) % len(dirs)]
        else:
            cur_pos = next_pos

    if loops:
        return visited
    else:
        print(len(visited))


def solve_part_two(area):
    n = len(area)
    visited = solve_part_one(area, True)
    new_obstacles = set()
    for i, vis in enumerate(visited):
        new_area = area.copy()
        row = list(new_area[vis[0]])
        row[vis[1]] = '#'
        new_area[vis[0]] = ''.join(row)
        if solve_part_one(new_area, True) == -1:
            new_obstacles.add(vis)

    print(len(new_obstacles))


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
