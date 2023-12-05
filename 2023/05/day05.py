def solve_part_one(seeds, maps):
    locations = []
    for seed in seeds:
        converted_num = seed
        for m in maps:
            for rule in m:
                if converted_num in range(rule[1], rule[1] + rule[2]):
                    converted_num = rule[0] + converted_num - rule[1]
                    break
        locations.append(converted_num)

    print(min(locations))


def solve_part_two(seeds, maps):
    lowest_locations = []
    for i in range(0, len(seeds) - 1, 2):
        seeds_ranges = [range(seeds[i], seeds[i] + seeds[i + 1])]
        converted_ranges = seeds_ranges
        for m in maps:
            old_ranges = converted_ranges
            new_ranges = []
            for rule in m:
                map_range = range(rule[1], rule[1] + rule[2])
                new_old_ranges = []
                for conv_range in old_ranges:
                    if not conv_range:
                        continue
                    if conv_range[0] in map_range and conv_range[-1] in map_range:
                        new_ranges.append(range(rule[0] + conv_range[0] - rule[1], rule[0] + conv_range[-1] - rule[1]))
                    elif map_range[0] in conv_range and map_range[-1] in conv_range:
                        new_old_ranges.append(range(conv_range[0], map_range[0]))
                        new_old_ranges.append(range(map_range[-1], conv_range[-1]))
                        new_ranges.append(range(rule[0] + map_range[0] - rule[1], rule[0] + map_range[-1] - rule[1]))
                    elif map_range[0] in conv_range:
                        new_old_ranges.append(range(conv_range[0], map_range[0]))
                        new_ranges.append(range(rule[0] + map_range[0] - rule[1], rule[0] + conv_range[-1] - rule[1]))
                    elif map_range[-1] in conv_range:
                        new_old_ranges.append(range(map_range[-1], conv_range[-1]))
                        new_ranges.append(range(rule[0] + conv_range[0] - rule[1], rule[0] + map_range[-1] - rule[1]))
                    else:
                        new_old_ranges.append(conv_range)
                old_ranges = new_old_ranges
            converted_ranges = old_ranges
            converted_ranges.extend(new_ranges)
        lowest_locations.append(min([x[0] for x in converted_ranges if x]))

    print(min(lowest_locations))


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().split('\n\n')]
    seeds = [int(x) for x in data[0][7:].split()]
    maps = [[(int(z.split()[0]), int(z.split()[1]), int(z.split()[2])) for z in y]
            for x in data[1:] for y in [x.splitlines()[1:]]]

    solve_part_one(seeds, maps)
    solve_part_two(seeds, maps)
