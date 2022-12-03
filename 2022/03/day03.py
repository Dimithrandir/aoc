def solve_part_one(data):
    p_sum = 0
    for ruck in data:
        for i in ruck[:len(ruck)//2]:
            if i in ruck[len(ruck)//2:]:
                p_sum += ord(i) - (96 if i.islower() else 38)
                break
    print(p_sum)

def solve_part_two(data):
    p_sum = 0
    i = 0
    while i <= len(data) - 3:
        for item in set(data[i] + data[i+1] + data[i+2]):
            if item in data[i] and item in data[i+1] and item in data[i+2]:
                p_sum += ord(item) - (96 if item.islower() else 38)
                break
        i += 3
    print(p_sum)

if __name__ == '__main__':
    with open('input') as file:
        data = file.read().splitlines()

    solve_part_one(data)
    solve_part_two(data)
