import re

fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

ecls = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def check_field(field, val):
    return (field == 'byr' and int(val) in range(1920, 2003) or
            field == 'iyr' and int(val) in range(2010, 2021) or
            field == 'eyr' and int(val) in range(2020, 2031) or
            field == 'hgt' and val[-2:] == 'cm' and int(val[:-2]) in range(150, 194) or
            field == 'hgt' and val[-2:] == 'in' and int(val[:-2]) in range(59, 77) or
            field == 'hcl' and len(val) == 7 and re.findall('#[0-9a-f]{6}', val) or
            field == 'ecl' and val in ecls or
            field == 'pid' and len(val) == 9 and re.findall('[0-9]{9}', val) or
            field == 'cid')


def solve_part_one(passports):
    count = 0
    for passport in passports:
        dif = fields.difference(passport.keys())
        if dif in [set(), {'cid'}]:
            count += 1
    print(count)


def solve_part_two(passports):
    count = 0
    for passport in passports:
        dif = fields.difference(passport.keys())
        if dif in [set(), {'cid'}]:
            if False not in [check_field(x, passport[x]) for x in passport.keys()]:
                count += 1
    print(count)


if __name__ == '__main__':
    with open('input') as file:
        data = [{z.split(':')[0]: z.split(':')[1] for z in y}
                for x in file.read().split('\n\n') for y in [x.split()]]

    solve_part_one(data)
    solve_part_two(data)
