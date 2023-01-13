from copy import deepcopy


def numbers_mix(sequence, amount):
    original = deepcopy(sequence)

    for _ in range(amount):
        for idx, num in original:
            old_pos = sequence.index((idx, num))
            popped = sequence.pop(old_pos)
            new_pos = (old_pos + num) % (len(original) - 1)
            sequence.insert(new_pos, popped)

    return sequence


def index_lookup(mixed, index):
    zero_element = list(filter(lambda x: x[1] == 0, mixed))[0]
    zero_index = mixed.index(zero_element)
    target = mixed[(zero_index + index) % len(mixed)][1]

    return target


def get_puzzle_input():
    with open('input.txt') as open_txt:
        data = open_txt.readlines()
        data = list(map(lambda x: (x[0], int(x[1].strip())), enumerate(data, 0)))

    return data


def solve_part_1(input):
    mixed = numbers_mix(input, 1)

    x = index_lookup(mixed, 1000)
    y = index_lookup(mixed, 2000)
    z = index_lookup(mixed, 3000)

    total = sum([x, y, z])

    return total


def solve_part_2(input):
    decrypted = list(map(lambda x: (x[0], x[1] * 811589153), input))
    mixed = numbers_mix(decrypted, 10)

    x = index_lookup(mixed, 1000)
    y = index_lookup(mixed, 2000)
    z = index_lookup(mixed, 3000)

    total = sum([x, y, z])

    return total


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
