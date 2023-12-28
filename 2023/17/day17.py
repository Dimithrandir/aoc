from heapq import heappush, heappop


direcs = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}


def get_neighbors(i, j, n):
    return [(i + x, j + y)
            for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if i + x in range(n) and j + y in range(n)]


def solve_part_one(city, min_blocks=0, max_blocks=3):
    n = len(city)
    m = len(city[0])
    graph = {}
    for i, row in enumerate(city):
        for j, block in enumerate(row):
            graph[(i, j)] = [(x, int(city[x[0]][x[1]])) for x in get_neighbors(i, j, n)]

    start = (0, 0)
    end = (n - 1, m - 1)
    distances = {}
    for node in graph.keys():
        for direction in '><v^':
            distances[(node, direction)] = 0 if node == start else 1_000_000
    queue = [(0, start, '>')]

    while queue:
        heat_loss, node, direction = heappop(queue)
        if heat_loss > distances[(node, direction)]:
            continue

        new_node = node
        for i in range(max_blocks):
            new_node = (new_node[0] + direcs[direction][0], new_node[1] + direcs[direction][1])
            if new_node[0] not in range(n) or new_node[1] not in range(m):
                break

            heat_loss += int(city[new_node[0]][new_node[1]])

            if i < min_blocks:
                continue

            for new_dir in '<>' if direction in 'v^' else 'v^':
                if heat_loss < distances[(new_node, new_dir)]:
                    distances[(new_node, new_dir)] = heat_loss
                    heappush(queue, (heat_loss, new_node, new_dir))

    print(min([distances[x] for x in distances.keys() if x[0] == end]))


def solve_part_two(city, min_blocks, max_blocks):
    solve_part_one(city, min_blocks, max_blocks)


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data, 3, 10)
