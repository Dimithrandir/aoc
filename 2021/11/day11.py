def solve_part_one(data):
    
    def flash(i, j):
        neighbors = [ (x, y) for x in range(i-1, i+2) for y in range(j-1, j+2) if (x, y) != (i, j) and x in range(len(data)) and y in range(len(data[0])) ]
        flashes = 0
        for (k, l) in neighbors:
            if data[k][l]:
                data[k][l] = (data[k][l] + 1) % 10
                if not data[k][l]:
                    flashes += 1 + flash(k, l)
        return flashes

    flashes = 0

    for step in range(100):
        flashed = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] = (data[i][j] + 1) % 10
                if not data[i][j]:
                    flashes += 1
                    flashed.append((i, j))

        for (i, j) in flashed:
            flashes += flash(i, j)
    
    print(flashes)

def solve_part_two(data):

    def flash(i, j):
        neighbors = [ (x, y) for x in range(i-1, i+2) for y in range(j-1, j+2) if (x, y) != (i, j) and x in range(len(data)) and y in range(len(data[0])) ]
        for (k, l) in neighbors:
            if data[k][l]:
                data[k][l] = (data[k][l] + 1) % 10
                if not data[k][l]:
                    flash(k, l)

    step = 0

    while True:
        step += 1
        flashed = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] = (data[i][j] + 1) % 10
                if not data[i][j]:
                    flashed.append((i, j))

        for (i, j) in flashed:
            flash(i, j)

        synced = True
        for row in data:
            for dumbo in row:
                if dumbo:
                    synced = False
                    break
            if not synced:
                break

        if synced:
            break
    
    print(step)

if __name__ == '__main__':
    with open('input') as file:
        data = [ [ int(y) for y in x ] for x in file.read().splitlines() ]

    # solve_part_one(data)
    solve_part_two(data)
