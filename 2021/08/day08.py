def solve_part_one(output_values):

    count = 0

    for digits in output_values:
        for digit in digits:
            if len(digit) == 7 or len(digit) > 1 and len(digit) < 5:
                count += 1

    print(count)

def solve_part_two(input_values, output_values):

    def intersect(str1, str2):
        return [ x for x in str1 if x in str2 ]

    def diff(str1, str2):
        return [ x for x in str1 if x not in str2 ]

    def decode(digit, key):
        dcd_str = ''
        for s in digit:
            for (k, v) in key.items():
                if v == s:
                    dcd_str += k
                    break
        dcd_str = sorted(dcd_str)

        if dcd_str == list('abcefg'):
            return 0
        elif dcd_str == list('acdeg'):
            return 2
        elif dcd_str == list('acdfg'):
            return 3
        elif dcd_str == list('abdfg'):
            return 5
        elif dcd_str == list('abdefg'):
            return 6
        elif dcd_str == list('abcdfg'):
            return 9

    count = 0

    for (i, digits) in enumerate(input_values):

        key = {}
        decoded = {}

        for digit in digits:
            if len(digit) == 7:
                decoded[8] = digit
            elif len(digit) == 3:
                decoded[7] = digit
            elif len(digit) == 4:
                decoded[4] = digit
            elif len(digit) == 2:
                decoded[1] = digit

        key['a'] = diff(decoded[7], decoded[1])[0]

        e_diff = diff(diff(decoded[8], decoded[4]), decoded[7])
        for digit in digits:
            if len(digit) == 6:
                temp_diff = diff(e_diff, digit)
                if temp_diff:
                    key['e'] = temp_diff[0]
                    break
        
        d_diff = diff(decoded[8], decoded[7])
        for digit in digits:
            if len(digit) == 6:
                temp_diff = diff(d_diff, digit)
                if temp_diff and temp_diff[0] != key['e'] :
                    key['d'] = temp_diff[0]
                    break

        key['b'] = diff(diff(decoded[4], decoded[1]), key.values())[0]

        key['g'] = diff(diff(decoded[8], decoded[1]), key.values())[0]

        for digit in digits:
            if len(digit) == 6:
                temp_diff = diff(decoded[1], digit)
                if temp_diff:
                    key['c'] = temp_diff[0]

        key['f'] = diff(decoded[8], key.values())[0]

        for digit in digits:
            if digit not in decoded.values():
                decoded[decode(digit, key)] = digit

        output_dig = ''
        for digit in output_values[i]:
            for (k, v) in decoded.items():
                if sorted(digit) == sorted(v):
                    output_dig += str(k)
                    break

        count += int(output_dig)
    
    print(count)
                
if __name__ == '__main__':
    with open('input') as file:
        data = [ x.split('|') for x in file.readlines() ]
        data_in = [ x[0].strip().split(' ') for x in data ]
        data_out = [ x[1].strip().split(' ') for x in data ]

    solve_part_one(data_out)
    solve_part_two(data_in, data_out)
