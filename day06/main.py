def solve_part_1(input, step):
    line_length = len(input)
    for i in range(line_length - step + 1):
        window = input[i:i+step]
        if len(window) == len(set(window)):
            return i + step


def solve_part_2(input, step):
    line_length = len(input)
    for i in range(line_length - step + 1):
        window = input[i:i + step]
        if len(window) == len(set(window)):
            return i + 14


def get_puzzle_input():
    with open("input.txt") as input_txt:
        return input_txt.readline()


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input, 4)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input, 14)
    print(f"Part 2: {answer_2}")