dirs = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}


def build_path(race_area):

    def get_neighbors(pos):
        return [(pos[0] + dirs[x][0], pos[1] + dirs[x][1]) for x in dirs.keys()
                if race_area[pos[0] + dirs[x][0]][pos[1] + dirs[x][1]] == '.'
                and pos[0] + dirs[x][0] in range(n)
                and pos[1] + dirs[x][1] in range(n)]

    n = len(race_area)
    start = (0, 0)
    end = (0, 0)
    track = []
    for i in range(n):
        for j in range(n):
            if race_area[i][j] == '.':
                track.append((i, j))
            elif race_area[i][j] == 'S':
                start = (i, j)
            elif race_area[i][j] == 'E':
                end = (i, j)

    path = [start]
    while track:
        next_i = track.index([x for x in get_neighbors(path[-1])
                              if x in track][0])
        path.append(track.pop(next_i))
    path.append(end)

    return path


def solve_part_one(race_area):
    path = build_path(race_area)
    result = 0

    for i, cur in enumerate(path):
        for d in dirs.keys():
            cheat_start = (cur[0] + dirs[d][0], cur[1] + dirs[d][1])
            cheat_end = (cur[0] + 2 * dirs[d][0], cur[1] + 2 * dirs[d][1])
            if (cheat_start not in path and cheat_end in path
                    and path.index(cur) < path.index(cheat_end)):
                if path.index(cheat_end) - path.index(cur) - 2 >= 100:
                    result += 1
    print(result)


def solve_part_two(race_area):
    path = build_path(race_area)
    result = 0

    for i, cur in enumerate(path):
        cheat_start = cur
        cur_i = path.index(cur)
        cheat_ends = [x for x in path
                      if abs(cur[0] - x[0]) + abs(cur[1] - x[1]) <= 20
                      and path.index(x) > cur_i
                      and x != cheat_start]
        for end in cheat_ends:
            end_i = path.index(end)
            track_ps = end_i - cur_i
            cheat_ps = abs(cheat_start[0] - end[0]) + abs(cheat_start[1] - end[1])
            saved_ps = track_ps - cheat_ps
            if saved_ps >= 100:
                result += 1
    print(result)


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
