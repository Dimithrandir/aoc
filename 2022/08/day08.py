def solve_part_one(trees):

    def is_visible(i, j, n):
        # up right down left
        for (axis, dim, to, step, dx, dy) in [('y', j, 0, -1, 0, -1), ('x', i, n-1, 1, 1, 0), ('y', j, n-1, 1, 0, 1), ('x', i, 0, -1, -1, 0)]:
            visible = True
            for dim in range(dim, to, step):
                if trees[i][j] <= trees[(dim if axis == 'x' else i) + dx][(dim if axis == 'y' else j) + dy]:
                    visible = False
                    break
            if visible:
                return True
        return False

    n = len(trees)
    count = 4 * (n - 1)
    for i in range(1, n-1):
        for j in range(1, n-1):
            if is_visible(i, j, n):
                count += 1
    print(count)

def solve_part_two(trees):

    def calc_score(i, j, n):
        score = 1
        # up right down left
        for (axis, dim, to, step, dx, dy) in [('y', j, 0, -1, 0, -1), ('x', i, n-1, 1, 1, 0), ('y', j, n-1, 1, 0, 1), ('x', i, 0, -1, -1, 0)]:
            count = 0
            for dim in range(dim, to, step):
                count += 1
                if trees[i][j] <= trees[(dim if axis == 'x' else i) + dx][(dim if axis == 'y' else j) + dy]:
                    break
            score *= count
        return score

    n = len(trees)
    print(max([ calc_score(i, j, n) for i in range(1, n-1) for j in range(1, n-1) ]))

if __name__ == '__main__':
    with open('input') as file:
        data = [ [ int(y) for y in list(x)] for x in file.read().splitlines() ]
    
    solve_part_one(data)
    solve_part_two(data)
