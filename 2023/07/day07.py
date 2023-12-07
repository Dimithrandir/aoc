strengths = 'AKQJT98765432'
strengths_jokers = 'AKQT98765432J'


def apply_jokers(hand):
    if hand == 'JJJJJ':
        return 'AAAAA'
    card_occurs = {key: list(set([x for x in hand if hand.count(x) == key and x != 'J']))
                   for key in range(1, 6)}
    max_occurs = max([x for x in card_occurs.keys() if card_occurs[x]])
    new_card = (card_occurs[max_occurs][0] if len(card_occurs[max_occurs]) == 1
                else strengths_jokers[min([strengths_jokers.index(x) for x in card_occurs[max_occurs]])])
    return hand.replace('J', new_card)


def get_type(hand, jokers):
    hand = apply_jokers(hand) if jokers and 'J' in hand else hand
    hand_type = 6
    hand_set = set(hand)
    diff_cards = len(hand_set)
    if diff_cards == 1:
        hand_type = 0
    elif diff_cards == 2:
        hand_type = min([hand.count(x) for x in hand])
    elif diff_cards == 3:
        hand_type = 6 - max([hand.count(x) for x in hand])
    elif diff_cards == 4:
        hand_type = 5

    return hand_type


def solve_part_one(hands, jokers=False):
    types = {key: [] for key in range(7)}
    cards = strengths_jokers if jokers else strengths
    for hand in hands:
        hand_type = get_type(hand[0], jokers)
        if not types[hand_type]:
            types[hand_type].append(hand[0])
            continue
        for i, prev_card in enumerate(types[hand_type]):
            first_diff_index = [x for x in range(5) if prev_card[x] != hand[0][x]][0]
            if cards.index(prev_card[first_diff_index]) > cards.index(hand[0][first_diff_index]):
                types[hand_type].insert(i, hand[0])
                break
        if hand[0] not in types[hand_type]:
            types[hand_type].append(hand[0])

    ranked_hands = list(reversed([y for x in types.keys() for y in types[x]]))
    total_wins = 0
    for hand in hands:
        total_wins += (ranked_hands.index(hand[0]) + 1) * hand[1]

    print(total_wins)


def solve_part_two(hands, jokers):
    solve_part_one(hands, jokers)


if __name__ == '__main__':
    with open('input') as file:
        data = [(y[0], int(y[1])) for x in file.read().splitlines() for y in [x.split(' ')]]

    solve_part_one(data)
    solve_part_two(data, True)
