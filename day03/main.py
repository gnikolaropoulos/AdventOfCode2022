import string

all_letters = string.ascii_letters
lettersToPriority = {}
priority = 1
for letter in all_letters:
    lettersToPriority.update({letter:priority})
    priority += 1


def solve_part_1(input):
    priority = 0
    for line in input:
        compartment_len = int(len(line)/2)
        first_compartment = line[:compartment_len]
        second_compartment = line[compartment_len:]
        common_items = set(list(first_compartment)).intersection(set(list(second_compartment)))
        for item in common_items:
            priority += lettersToPriority.get(item)
    return priority


def solve_part_2(input):
    i = 0
    priority = 0
    while i < len(input):
        common_items = set(list(input[i])).intersection(set(list(input[i + 1])).intersection(set(list(input[i + 2]))))
        i += 3
        for item in common_items:
            priority += lettersToPriority.get(item)
    return priority


def get_puzzle_input():
    return [x.strip() for x in open('input.txt')]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")