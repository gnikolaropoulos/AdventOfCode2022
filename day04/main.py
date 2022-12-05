def solve_part_1(input):
    count = 0
    for line in input:
        if (line[0] <= line[2] and line[1] >= line[3]) or (line[0] >= line[2] and line[1] <= line[3]):
            count += 1
    return count


def solve_part_2(input):
    count = 0
    for line in input:
        if (line[0] <= line[2] and line[1] >= line[3]) or (line[0] >= line[2] and line[1] <= line[3]):
            count += 1
        elif line[2] <= line[0] <= line[3]:
            count += 1
        elif line[0] <= line[2] <= line[1]:
            count += 1
    return count


def get_puzzle_input():
    pairs = []
    lines = [x.strip() for x in open("input.txt")]
    for line in lines:
        (left_elf, right_elf) = line.split(",")
        pairs.append([int(left_elf.split("-")[0]), int(left_elf.split("-")[1]),
                      int(right_elf.split("-")[0]), int(right_elf.split("-")[1])])
    return pairs


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")