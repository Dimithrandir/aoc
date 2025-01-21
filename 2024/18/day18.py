from heapq import heappush, heappop


dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}


def get_neighbors(space, n, corrupted):
    return [(space[0] + dirs[x][0], space[1] + dirs[x][1])
            for x in dirs.keys()
            if (space[1] + dirs[x][1], space[0] + dirs[x][0]) not in corrupted
            and space[0] + dirs[x][0] in range(n)
            and space[1] + dirs[x][1] in range(n)]


def find_path(start, end, n, corrupted):
    dist = {}
    prev = {}
    queue = [start]
    for i in range(n):
        for j in range(n):
            if (i, j) in dist.keys():
                continue
            dist[(i, j)] = 10**10
            prev[(i, j)] = None
    dist[start] = 0

    while queue:
        cur = heappop(queue)
        if cur == end:
            break
        neighbors = get_neighbors(cur, n, corrupted)
        for neigh in neighbors:
            alt = dist[cur] + 1
            if alt < dist[neigh]:
                dist[neigh] = alt
                prev[neigh] = cur
                heappush(queue, neigh)

    path = [end]
    cur = end
    while prev[cur]:
        cur = prev[cur]
        path.append(cur)

    return path


def solve_part_one(positions):
    n = max([y for x in positions for y in x]) + 1
    start = (0, 0)
    end = (n - 1, n - 1)
    corrupted = positions[:1024]
    path = find_path(start, end, n, corrupted)
    print(len(path) - 1)


def solve_part_two(positions):
    n = max([y for x in positions for y in x]) + 1
    start = (0, 0)
    end = (n - 1, n - 1)
    corrupted = []
    path = find_path(start, end, n, corrupted)

    for byte in positions:
        corrupted.append(byte)
        if tuple(reversed(byte)) not in path:
            continue
        path = find_path(start, end, n, corrupted)
        if not len(path) - 1:
            print(byte)
            return


if __name__ == '__main__':
    with open('input') as file:
        data = [tuple([int(y) for y in x.split(',')])
                for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
