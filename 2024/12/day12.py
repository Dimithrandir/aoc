dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_region(m, plot, region=[]):
    if plot not in region:
        region.append(plot)
    n = len(m)
    neighbors = [(plot[0] + x[0], plot[1] + x[1]) for x in dirs
                 if plot[0] + x[0] in range(n)
                 and plot[1] + x[1] in range(n)
                 and m[plot[0] + x[0]][plot[1] + x[1]] == m[plot[0]][plot[1]]
                 and (plot[0] + x[0], plot[1] + x[1]) not in region]
    for neigh in neighbors:
        find_region(m, neigh, region)

    return region


def get_perimeter(m, region):
    perimeter = 0
    n = len(m)
    for plot in region:
        fences = [(plot[0] + x[0], plot[1] + x[1]) for x in dirs
                  if (plot[0] + x[0] in range(n)
                  and plot[1] + x[1] in range(n)
                  and m[plot[0] + x[0]][plot[1] + x[1]] != m[plot[0]][plot[1]]
                  and (plot[0] + x[0], plot[1] + x[1]) not in region)
                  or plot[0] + x[0] not in range(n)
                  or plot[1] + x[1] not in range(n)]
        perimeter += len(fences)
    return perimeter


def get_sides(m, region):
    sides = 0
    fences = []
    n = len(m)
    for plot in region:
        fences += [(plot[0] + x[0], plot[1] + x[1]) for x in dirs
                   if (plot[0] + x[0] in range(n)
                   and plot[1] + x[1] in range(n)
                   and m[plot[0] + x[0]][plot[1] + x[1]] != m[plot[0]][plot[1]]
                   and (plot[0] + x[0], plot[1] + x[1]) not in region)
                   or plot[0] + x[0] not in range(n)
                   or plot[1] + x[1] not in range(n)]

    i_range = range(min(fences, key=lambda l: l[0])[0],
                    max(fences, key=lambda l: l[0])[0] + 1)
    j_range = range(min(fences, key=lambda l: l[1])[1],
                    max(fences, key=lambda l: l[1])[1] + 1)

    for i in i_range:
        i_fences_up = list(set([x for x in fences
                                if x[0] == i
                                and (x[0] + 1, x[1]) in region]))
        i_fences_down = list(set([x for x in fences
                                  if x[0] == i
                                  and (x[0] - 1, x[1]) in region]))
        if not (i_fences_up + i_fences_down):
            continue
        i_fences_up.sort(key=lambda l: l[1])
        i_fences_down.sort(key=lambda l: l[1])
        line_sides = 2 if i_fences_up and i_fences_down else 1
        for k in range(1, len(i_fences_up)):
            if i_fences_up[k][1] != i_fences_up[k-1][1] + 1:
                line_sides += 1
        for k in range(1, len(i_fences_down)):
            if i_fences_down[k][1] != i_fences_down[k-1][1] + 1:
                line_sides += 1
        sides += line_sides

    for j in j_range:
        j_fences_left = list(set([x for x in fences
                                  if x[1] == j
                                  and (x[0], x[1] + 1) in region]))
        j_fences_right = list(set([x for x in fences
                                   if x[1] == j
                                   and (x[0], x[1] - 1) in region]))
        if not (j_fences_left + j_fences_right):
            continue
        j_fences_left.sort(key=lambda l: l[0])
        j_fences_right.sort(key=lambda l: l[0])
        line_sides = 2 if j_fences_left and j_fences_right else 1
        for k in range(1, len(j_fences_left)):
            if j_fences_left[k][0] != j_fences_left[k-1][0] + 1:
                line_sides += 1
        for k in range(1, len(j_fences_right)):
            if j_fences_right[k][0] != j_fences_right[k-1][0] + 1:
                line_sides += 1
        sides += line_sides

    return sides


def solve_part_one(garden, discount=False):
    regions = []
    passed = []
    total_price = 0
    n = len(garden)

    for i in range(n):
        for j in range(n):
            if (i, j) in passed:
                continue
            new_reg = find_region(garden, (i, j), [])
            regions.append(new_reg)
            passed += new_reg

    for region in regions:
        total_price += len(region) * (get_sides(garden, region)
                                      if discount
                                      else get_perimeter(garden, region))
    print(total_price)


def solve_part_two(garden, discount=True):
    solve_part_one(garden, discount)


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
