def get_neighbors(i, j, n, m):
    neighbors = []
    if i < n - 1:
        neighbors.append((i+1, j))
    if i > 0:
        neighbors.append((i-1, j))
    if j < m - 1:
        neighbors.append((i, j+1))
    if j > 0:
        neighbors.append((i, j-1))
    return neighbors

def find_distances(graph, start):

    distances = { x : 100000 for x in list(graph.keys())}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        (p, q) = (-1, -1)

        for node in unvisited:
            if (p, q) == (-1, -1):
                (p, q) = node
            elif distances[node] < distances[(p, q)]:
                (p, q) = node

        for (r, s) in graph[(p, q)]:
            new_dist = distances[(p, q)] + 1
            if new_dist < distances[(r, s)]:
                distances[(r, s)] = new_dist

        unvisited.remove((p, q))

    return distances

def solve_part_one(grid):

    n = len(grid)
    m = len(grid[0])
    graph = {}
    (start, end) = 2 * [(-1, -1)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'E':
                end = (i, j)
                grid[i][j] = 'z'
            elif grid[i][j] == 'S':
                start = (i, j)
                grid[i][j] = 'a'

    for i in range(n):
        for j in range(m):
            if (i, j) == end:
                graph[end] = []
                continue
            graph[(i, j)] = [ x for x in get_neighbors(i, j, n, m) if ord(grid[x[0]][x[1]]) <= ord(grid[i][j]) + 1 ]

    distances = find_distances(graph, start)
    print(distances[end])

def solve_part_two(grid):

    n = len(grid)
    m = len(grid[0])
    graph = {}
    start = (-1, -1)
    ends = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'E':
                start = (i, j)
                grid[i][j] = 'z'
            elif grid[i][j] in ['S', 'a']:
                ends.append((i, j))
                grid[i][j] = 'a'

    for i in range(n):
        for j in range(m):
            if (i, j) in ends:
                graph[(i, j)] = []
                continue
            graph[(i, j)] = [ x for x in get_neighbors(i, j, n, m) if ord(grid[x[0]][x[1]]) >= ord(grid[i][j]) - 1 ]

    distances = find_distances(graph, start)
    print(min([ distances[x] for x in ends ]))

if __name__ == '__main__':
    with open('input') as file:
        data = [ [ y for y in x ] for x in file.read().splitlines() ]

    solve_part_one(data)
    solve_part_two(data)
