dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def solve_part_one(m):
    n = len(m)
    count = 0
    for i in range(n):
        for j in range(n):
            if m[i][j] == 'X':
                for d in dirs:
                    k = i + 3 * d[0]
                    l = j + 3 * d[1]
                    if (
                            k in range(n) and l in range(n)
                            and '%s%s%s' % (
                                m[k - 2 * d[0]][l - 2 * d[1]],
                                m[k - d[0]][l - d[1]],
                                m[k][l]) == 'MAS'
                            ):
                        count += 1
    print(count)


def solve_part_two(m):
    n = len(m)
    count = 0
    x_dirs = [x for i, x in enumerate(dirs) if i % 2]
    for i in range(n):
        for j in range(n):
            if m[i][j] == 'A':
                mases = []
                for d in x_dirs:
                    k = i - d[0]
                    l = j - d[1]
                    p = i + d[0]
                    q = j + d[1]
                    mases.append(k in range(n) and l in range(n)
                                 and p in range(n) and q in range(n)
                                 and '%s%s%s' % (m[k][l], m[i][j], m[p][q]) == 'MAS')
                if (mases[0] or mases[2]) and (mases[1] or mases[3]):
                    count += 1
    print(count)


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
