brackets = ['()', '[]', '{}', '<>']
scores_error = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores_autoc = {')': 1, ']': 2, '}': 3, '>': 4}

def clean_up_pairs(line):
    temp_line = line
    while True:
        new_line = temp_line
        for pair in brackets:
            new_line = new_line.replace(pair, '')
        if new_line == temp_line:
            break
        temp_line = new_line
    return new_line

def solve_part_one(lines):

    score = 0
    
    for line in lines:
        for b in clean_up_pairs(line):
            if b in scores_error.keys():
                score += scores_error[b]
                break

    print(score)

def solve_part_two(lines):

    scores = []
    
    for line in lines:

        score = 0
        autocomplete = ''
        
        # find autocomplete string
        for b in clean_up_pairs(line):
            if b in scores_autoc.keys():
                autocomplete = ''
                break
            else:
                autocomplete = b + autocomplete

        # calculate score
        if autocomplete:
            for b in autocomplete:
                for pair in brackets:
                    if pair[0] == b:
                        score = score * 5 + scores_autoc[pair[1]]
                        break
            scores.append(score)

    print(sorted(scores)[int(len(scores)/2)])

if __name__ == '__main__':
    with open('input') as file:
        data = file.read().splitlines()

    solve_part_one(data)
    solve_part_two(data)
