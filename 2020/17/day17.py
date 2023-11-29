def solve_part_one(initial):

    def get_neighbors(i, j, k):
        return set([(x, y, z) for x in range(i-1, i+2) for y in range(j-1, j+2) for z in range(k-1, k+2) if (x, y, z) != (i, j, k)])

    activated = set()
    for i, row in enumerate(initial):
        for j, cube in enumerate(row):
            if cube == '#':
                activated.add((i, j, 0))
    activated_new = activated.copy()

    for turn in range(6):
        xs = sorted([a[0] for a in activated])
        ys = sorted([a[1] for a in activated])
        zs = sorted([a[2] for a in activated])
        x_range = range(min(xs) - 1, max(xs) + 2)
        y_range = range(min(ys) - 1, max(ys) + 2)
        z_range = range(min(zs) - 1, max(zs) + 2)

        for i in x_range:
            for j in y_range:
                for k in z_range:
                    if (i, j, k) in activated and len(get_neighbors(i, j, k).intersection(activated)) not in range(2, 4):
                        activated_new.remove((i, j, k))
                    if (i, j, k) not in activated and len(get_neighbors(i, j, k).intersection(activated)) == 3:
                        activated_new.add((i, j, k))
        activated = activated_new.copy()

    print(len(activated))


def solve_part_two(initial):

    def get_neighbors(i, j, k, l):
        return set([(x, y, z, w) for x in range(i-1, i+2) for y in range(j-1, j+2) for z in range(k-1, k+2) for w in range(l-1, l+2) if (x, y, z, w) != (i, j, k, l)])

    activated = set()
    for i, row in enumerate(initial):
        for j, cube in enumerate(row):
            if cube == '#':
                activated.add((i, j, 0, 0))
    activated_new = activated.copy()

    for turn in range(6):
        xs = sorted([a[0] for a in activated])
        ys = sorted([a[1] for a in activated])
        zs = sorted([a[2] for a in activated])
        ws = sorted([a[3] for a in activated])
        x_range = range(min(xs) - 1, max(xs) + 2)
        y_range = range(min(ys) - 1, max(ys) + 2)
        z_range = range(min(zs) - 1, max(zs) + 2)
        w_range = range(min(ws) - 1, max(ws) + 2)

        for i in x_range:
            for j in y_range:
                for k in z_range:
                    for l in w_range:
                        if (i, j, k, l) in activated and len(get_neighbors(i, j, k, l).intersection(activated)) not in range(2, 4):
                            activated_new.remove((i, j, k, l))
                        if (i, j, k, l) not in activated and len(get_neighbors(i, j, k, l).intersection(activated)) == 3:
                            activated_new.add((i, j, k, l))
        activated = activated_new.copy()

    print(len(activated))


if __name__ == '__main__':
    with open('input') as file:
        data = [y for x in file.read().splitlines() for y in [x]]

    solve_part_one(data)
    solve_part_two(data)
