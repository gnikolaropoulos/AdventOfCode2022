def solve_part_1(input):
    return max(map(sum, input))


def solve_part_2(input):
    return sum(sorted(map(sum, input), reverse=True)[:3])


def get_puzzle_input():
    with open("input.txt") as input_txt:
        groups = [list(map(int, g.split('\n')))
                  for g in input_txt.read().split('\n\n')]
    return groups


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
