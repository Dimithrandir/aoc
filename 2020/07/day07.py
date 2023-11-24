def build_rules_dict(rules):
    rules_dict = {}
    for rule in rules:
        rule_list = rule.split(' bags contain ')
        rules_dict[rule_list[0]] = {}
        if rule_list[1] == 'no other bags.':
            continue
        for content in rule_list[1].split(','):
            content_list = content.strip().split(' ')
            color_name = content_list[1] + ' ' + content_list[2]
            rules_dict[rule_list[0]][color_name] = int(content_list[0])
    return rules_dict


def solve_part_one(rules):

    def find_bags(colors):
        containers = set()
        for (bag, content) in rules.items():
            if colors.intersection(content.keys()):
                containers.add(bag)
        return containers.union(find_bags(containers)) if containers else set()

    print(len(find_bags({'shiny gold'})))


def solve_part_two(rules):

    def count_sub_bags(bag):
        if not rules[bag].values():
            return 1
        total = 1
        for (key, value) in rules[bag].items():
            total += (value * count_sub_bags(key))
        return total

    print(count_sub_bags('shiny gold') - 1)


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]
        rules = build_rules_dict(data)

    solve_part_one(rules)
    solve_part_two(rules)
