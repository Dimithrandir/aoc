def man_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve_part_one(positions):
    
    row = 2000000
    x_min = min([ x[0] for x in positions.values() ])
    x_max = max([ x[0] for x in positions.values() ])
    count = 0

    beacons_man_dists = { k : man_dist(k, v) for (k, v) in positions.items() }

    for (sensor, distance) in beacons_man_dists.items():
        if sensor[0] - distance < x_min:
            x_min = sensor[0] - distance
        if sensor[0] + distance > x_max:
            x_max = sensor[0] + distance

    for i in range(x_min, x_max + 1):
        for (sensor, beacon) in positions.items():
            if man_dist(sensor, (i, row)) <= man_dist(sensor, beacon) and (i, row) not in positions.keys() and (i, row) not in positions.values():
                count += 1
                break

    print(count)

def get_limits(sensor, distance, x_min, x_max, y_min, y_max):
    xs = [ x for x in range(sensor[0] - distance, sensor[0] + distance)]
    xs.extend([ x for x in range(sensor[0] + distance, sensor[0] - distance, -1)])
    ys = [ y for y in range(sensor[1], sensor[1] + distance)]
    ys.extend([ y for y in range(sensor[1] + distance, sensor[1] - distance, -1)])
    ys.extend([ y for y in range(sensor[1] - distance, sensor[1])])

    return [ (xs[x], ys[x]) for x in range(len(xs)) if xs[x] >= x_min and xs[x] <= x_max and ys[x] >= y_min and ys[x] <= y_max ]

def solve_part_two(positions):

    (x_min, y_min) = 2 * [0]
    (x_max, y_max) = 2 * [4000000]

    beacons_man_dists = { k : man_dist(k, v) for (k, v) in positions.items() }

    beacons_limit_coords = {}
    for (k, v) in beacons_man_dists.items():
        beacons_limit_coords[k] = get_limits(k, v + 1, x_min, x_max, y_min, y_max)

    limits = []
    for coords in beacons_limit_coords.values():
        for coord in coords:
            limits.append(coord)

    beacon = (0, 0)
    for (i, coord) in enumerate(limits):
        outside = True
        for (sensor, dist) in beacons_man_dists.items():
            if man_dist(coord, sensor) <= dist:
                outside = False
                break
        if outside:
            beacon = coord
            break

    print(beacon[0] * 4000000 + beacon[1])

if __name__ == '__main__':
    with open('input') as file:
        data = { (int(x.split('=')[1].split(',')[0]), int(x.split('=')[2].split(':')[0])) : (int(x.split('=')[3].split(',')[0]), int(x.split('=')[4])) for x in file.read().splitlines() }

    solve_part_one(data)
    solve_part_two(data)
