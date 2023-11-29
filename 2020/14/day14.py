def get_mask_bits(mask, bits):
    return {key: [i for i, v in enumerate(reversed(mask)) if v == key] for key in bits}


def get_bin_str(num, length):
    num_str = bin(num)[2:]
    return (length - len(num_str)) * '0' + num_str


def apply_mask(num, mask_bit):
    for bit, indices in mask_bit.items():
        for i in indices:
            num = num[:35-i] + bit + num[36-i:]
    return num


def solve_part_one(program):
    mem = {}
    mask = ''

    for inst in program:
        if inst[0] == 'mask':
            mask = inst[1]
        else:
            num_str = get_bin_str(inst[1], 36)
            num_str = apply_mask(num_str, get_mask_bits(mask, ['0', '1']))
            mem[inst[0]] = int(num_str, 2)

    print(sum(mem.values()))


def solve_part_two(program):
    mem = {}
    mask = ''

    for inst in program:
        if inst[0] == 'mask':
            mask = inst[1]
        else:
            num_str = get_bin_str(inst[0], 36)
            mask_bits = get_mask_bits(mask, ['1', 'X'])
            num_str = apply_mask(num_str, mask_bits)

            for i in range(2 ** num_str.count('X')):
                i_str = get_bin_str(i, len(mask_bits['X']))
                new_num_str = num_str
                k = 0
                for j in mask_bits['X']:
                    new_num_str = new_num_str[:35-j] + i_str[k] + new_num_str[36-j:]
                    k += 1

                mem[int(new_num_str, 2)] = inst[1]

    print(sum(mem.values()))


if __name__ == '__main__':
    with open('input') as file:
        data = [(y[0], y[1]) if y[0] == 'mask' else (int(y[0][4:-1]), int(y[1])) for x in file.read().splitlines() for y in [x.split(' = ')]]

    solve_part_one(data)
    solve_part_two(data)
