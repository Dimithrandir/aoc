def solve_part_one(buffer):
    for i in range(3, len(buffer)):
        if len(set(buffer[i-3:i+1])) == 4:
            print(i+1)
            break

def solve_part_two(buffer):
    for i in range(13, len(buffer)):
        if len(set(buffer[i-13:i+1])) == 14:
            print(i+1)
            break

if __name__ == '__main__':
    with open('input') as file:
        data = file.read().strip()

    solve_part_one(data)
    solve_part_two(data)
