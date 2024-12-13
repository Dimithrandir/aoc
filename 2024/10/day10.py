dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def map_trails(m):
    n = len(m)
    graph = {}
    heads = []
    for i in range(n):
        for j in range(n):
            if m[i][j] == '0':
                heads.append((i, j))
            neighbors = [(i+x[0], j+x[1]) for x in dirs
                         if i + x[0] in range(n) and j + x[1] in range(n)
                         and int(m[i+x[0]][j+x[1]]) == int(m[i][j]) + 1]
            if neighbors:
                graph[(i, j)] = neighbors
    return graph, heads


def hike(graph, topmap, head, rating=False):
    if head not in graph.keys():
        if rating:
            return 1 if topmap[head[0]][head[1]] == '9' else 0
        else:
            return {head} if topmap[head[0]][head[1]] == '9' else set()
    else:
        total = 0 if rating else set()
        for pos in graph[head]:
            if rating:
                total += hike(graph, topmap, pos, rating)
            else:
                total |= hike(graph, topmap, pos, rating)
        return total


def solve_part_one(topmap, rating=False):
    trailgraph, trailheads = map_trails(topmap)
    total = 0
    for trailhead in trailheads:
        score = hike(trailgraph, topmap, trailhead, rating)
        total += score if rating else len(score)
    print(total)


def solve_part_two(topmap):
    solve_part_one(topmap, rating=True)


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
