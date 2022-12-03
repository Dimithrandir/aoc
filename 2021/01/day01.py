def solve_part_one(data):
    inc = 0
    for i in range(1, len(data)):
        if int(data[i]) > int(data[i-1]):
            inc += 1
    print(inc)

def solve_part_two(data):

    def sum_sw(a, b):
        s = 0
        for i in range(a, b+1):
            s += int(data[i])
        print(s)
        return s

    inc = 0
    for i in range(3, len(data)):
        if sum_sw(i-2, i) > sum_sw(i-3, i-1):
            inc += 1
    print(inc)

if __name__ == "__main__":
    with open("input") as file:
        solve_part_one(file.read().splitlines())
        solve_part_two(file.read().splitlines())
