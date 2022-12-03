def solve_part_one(hmap):

    risk_sum = 0

    for i in range(len(hmap)):
        for j in range(len(hmap[i])):
            neighs = []
            if i:
                neighs.append(hmap[i-1][j])
            if j < len(hmap[i]) - 1: 
                neighs.append(hmap[i][j+1])
            if i < len(hmap) - 1:
                neighs.append(hmap[i+1][j])
            if j:
                neighs.append(hmap[i][j-1])

            if hmap[i][j] < min(neighs):
                risk_sum += int(hmap[i][j]) + 1

    print(risk_sum)

def solve_part_two(hmap):
    
    # get neighbors coordinates
    def get_neighbors(i, j):
        neighs = []
        if i:
            neighs.append((i-1, j))
        if j < len(hmap[i]) - 1: 
            neighs.append((i, j+1))
        if i < len(hmap) - 1:
            neighs.append((i+1, j))
        if j:
            neighs.append((i, j-1))

        return neighs

    basins = {}
    sinks = []

    # find low points
    for i in range(len(hmap)):
        for j in range(len(hmap[i])):
            if hmap[i][j] < min([ hmap[x[0]][x[1]] for x in get_neighbors(i, j)]):
                sinks.append((i, j))
                basins[(i, j)] = []

    for i in range(len(hmap)):
        for j in range(len(hmap[i])):
            # 9's are out of basins
            if int(hmap[i][j]) != 9:
                p, q = i, j
                new_points = []
                # walk to lowest point
                while (p, q) not in sinks and (p, q) not in basins.values():
                    # add lowest neighbor to basin
                    min_val = 9
                    r, s = 0, 0
                    for coords in get_neighbors(p, q):
                        if int(hmap[coords[0]][coords[1]]) < min_val:
                            min_val = int(hmap[coords[0]][coords[1]])
                            (r, s) = (coords[0], coords[1])
                    new_points.append((r, s))
                    # next lowest point
                    (p, q) = (r, s)
                # add self to basin
                new_points.append((i, j))
                # avoid duplicates
                basins[(p, q)].extend([ x for x in new_points if x not in basins[(p, q)]])

    # sort basins by size
    sorted_basins = {key: val for key, val in sorted(basins.items(), key=lambda x: len(x[1]), reverse=True)}

    product = 1
    for basin in [ x for x in sorted_basins.values()][:3]:
        product *= len(basin)
            
    print(product)

if __name__ == '__main__':
    with open('input') as file:
        data = [ list(x) for x in file.read().splitlines() ]

    solve_part_one(data)
    solve_part_two(data)
