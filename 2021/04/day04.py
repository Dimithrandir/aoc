def check_bingo(numbers, matrix, n):
    # check rows
    for row in matrix:
        full_row = True
        for col in row:
            if col not in numbers[:n+1]:
                full_row = False
                break
        if full_row:
            return True
    # check columns
    for j in range(len(matrix[0])):
        full_col = True
        for i in range(len(matrix)):
            if matrix[i][j] not in numbers[:n+1]:
                full_col = False
                break
        if full_col:
            return True

    return False

def sum_unmarked(matrix, numbers):
    s = 0
    for row in matrix:
        for col in row:
            if col not in numbers:
                s += col
    return s

def solve_part_one(numbers, matrices):
    for i, number in enumerate(numbers):
        for matrix in matrices:
            if check_bingo(numbers, matrix, i):
                print(number * sum_unmarked(matrix, numbers[:i+1]))
                return

def solve_part_two(numbers, matrices):
    for i in range(len(numbers)-1, -1, -1):
        for j, matrix in enumerate(matrices):
            if not check_bingo(numbers, matrix, i):
                print(numbers[i+1] * sum_unmarked(matrices[j], numbers[:i+2]))
                return

if __name__ == '__main__':

    with open('input') as file:
        lines = file.read().splitlines()
        numbers = [ int(x) for x in lines[0].split(',') ] 
        matrices = []
        matrix = []
        for i in range(2, len(lines)):
            if lines[i] == '':
                matrices.append(matrix)
                matrix = []
            else:
                matrix.append([ int(x) for x in lines[i].split(' ') if x != ''])
        matrices.append(matrix)

    solve_part_one(numbers, matrices)
    solve_part_two(numbers, matrices)
