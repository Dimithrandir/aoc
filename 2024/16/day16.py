dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}


def map_maze(maze):
    n = len(maze)
    m = len(maze[0])
    nodes = []
    start = ()
    end = ()
    for i in range(n):
        for j in range(m):
            if maze[i][j] in '.SE':
                if maze[i][j] == 'S':
                    start = (i, j)
                if maze[i][j] == 'E':
                    end = (i, j)
                neighbors = [(i + dirs[x][0], j + dirs[x][1]) for x in dirs.keys()
                             if maze[i+dirs[x][0]][j+dirs[x][1]] in '.SE']
                if (len(neighbors) == 2
                    and (neighbors[0][0] == neighbors[1][0]
                         or neighbors[0][1] == neighbors[1][1])):
                    continue
                for k in dirs.keys():
                    nodes.append(((i, j), k))
    return start, end, nodes


def build_graph(nodes, maze):
    graph = {}
    for node in nodes:
        if node not in graph.keys():
            graph[node] = []

        dirs_keys = list(dirs.keys())
        op_dir = dirs_keys[(dirs_keys.index(node[1]) + 2) % len(dirs_keys)]

        for d in dirs:
            if d == op_dir:
                continue

            i = node[0][0]
            j = node[0][1]
            while i in range(len(maze)) and j in range(len(maze[0])):
                if d == '>':
                    j += 1
                elif d == '<':
                    j -= 1
                elif d == 'v':
                    i += 1
                elif d == '^':
                    i -= 1

                if maze[i][j] == '#':
                    break
                if ((i, j), d) in nodes:
                    graph[node].append(((i, j), d))
                    break
    return graph


def solve_part_one(maze):
    start, end, nodes = map_maze(maze)
    graph = build_graph(nodes, maze)

    start = (start, '>')
    dist = {x: 10**10 for x in list(graph.keys())}
    dist[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        cur = min([x for x in dist.keys() if x in unvisited], key=lambda l: dist[l])
        if cur[0] == end:
            break
        unvisited.remove(cur)

        for neigh in [x for x in graph[cur] if x in unvisited]:
            alt = (dist[cur]
                   + max(abs(cur[0][0] - neigh[0][0]), abs(cur[0][1] - neigh[0][1])))

            if cur[1] != neigh[1]:
                alt += 1000

            if alt < dist[neigh]:
                dist[neigh] = alt

    score = min([dist[x] for x in dist.keys() if x[0] == end])
    print(score)


def solve_part_two(maze):

    def find_tiles(prev, cur):
        tiles = set()
        if not prev[cur]:
            return tiles
        for p in prev[cur]:
            if cur[0][0] == p[0][0]:
                tiles_list = [(cur[0][0], x)
                              for x in range(min(cur[0][1], p[0][1]),
                                             max(cur[0][1], p[0][1]) + 1)]
            elif cur[0][1] == p[0][1]:
                tiles_list = [(x, cur[0][1])
                              for x in range(min(cur[0][0], p[0][0]),
                                             max(cur[0][0], p[0][0]) + 1)]
            tiles |= set(tiles_list) | find_tiles(prev, p)
        return tiles

    start, end, nodes = map_maze(maze)
    graph = build_graph(nodes, maze)

    start = (start, '>')
    dist = {x: 10**10 for x in list(graph.keys())}
    prev = {x: [] for x in list(graph.keys())}
    dist[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        cur = min([x for x in dist.keys() if x in unvisited], key=lambda l: dist[l])
        if cur[0] == end:
            break
        unvisited.remove(cur)

        for neigh in [x for x in graph[cur] if x in unvisited]:
            alt = (dist[cur]
                   + max(abs(cur[0][0] - neigh[0][0]), abs(cur[0][1] - neigh[0][1])))

            if cur[1] != neigh[1]:
                alt += 1000

            if alt <= dist[neigh]:
                if alt < dist[neigh]:
                    dist[neigh] = alt
                    prev[neigh] = []
                dist[neigh] = alt
                prev[neigh].append(cur)

    end_nodes = [x for x in nodes if x[0] == end and dist[x] < 10**10]
    for e in end_nodes:
        all_tiles = find_tiles(prev, e)
        print(len(all_tiles))


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
