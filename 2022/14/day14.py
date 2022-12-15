sand_hole = (500, 0)

def trace_path(points):
    trace = points
    for i in range(len(points) - 1):
        if points[i][0] == points[i+1][0]:
            trace.extend([ (points[i][0], y) for y in range(min(points[i][1], points[i+1][1]) + 1, max(points[i][1], points[i+1][1])) ])
        if points[i][1] == points[i+1][1]:
            trace.extend([ (x, points[i][1]) for x in range(min(points[i][0], points[i+1][0]) + 1, max(points[i][0], points[i+1][0])) ])
    return trace

def get_fall_pos(point):
    return [ (point[0], point[1] + 1), (point[0] - 1, point[1] + 1), (point[0] + 1, point[1] + 1) ]

def solve_part_one(paths):

    n = max([ y[1] for x in paths for y in x ])
    sand = []
    rock = []
    for path in paths:
        rock.extend(trace_path(path))

    while True:
        new_grain = sand_hole
        abyss = False
        while True:
            if new_grain[1] > n:
                abyss = True
                break
            fall_pos = get_fall_pos(new_grain)
            if fall_pos[0] not in rock and fall_pos[0] not in sand:
                new_grain = fall_pos[0]
            elif fall_pos[1] not in rock and fall_pos[1] not in sand:
                new_grain = fall_pos[1]
            elif fall_pos[2] not in rock and fall_pos[2] not in sand:
                new_grain = fall_pos[2]
            else:
                sand.append(new_grain)
                break
        if abyss:
            break

    print(len(sand))

def solve_part_two(paths):

    floor = max([ y[1] for x in paths for y in x ]) + 2
    rock = []
    for path in paths:
        rock.extend(trace_path(path))
    bottom_row = [sand_hole]
    grain_count = 1

    while bottom_row:
        new_grains = []
        for grain in [ x for x in bottom_row ]:
            fall_pos = get_fall_pos(grain)
            if fall_pos[0] not in rock and fall_pos[0] not in bottom_row and fall_pos[0][1] < floor:
                new_grains.append(fall_pos[0])
            if fall_pos[1] not in rock and fall_pos[1] not in bottom_row and fall_pos[1][1] < floor:
                new_grains.append(fall_pos[1])
            if fall_pos[2] not in rock and fall_pos[2] not in bottom_row and fall_pos[2][1] < floor:
                new_grains.append(fall_pos[2])
            bottom_row.remove(grain)
        grain_count += len(set(new_grains))
        bottom_row.extend(list(set(new_grains)))

    print(grain_count)

if __name__ == '__main__':
    with open('input') as file:
        data = [ [ (int(y.split(',')[0]), int(y.split(',')[1])) for y in x.split(' -> ') ] for x in file.read().splitlines() ]

    solve_part_one(data)
    solve_part_two(data)
