register_values = {}


def solve_part_1(input):
    register_x = 1
    clock_cycle = 1
    for line in input:
        if line == "noop":
            cycle_duration = 1
        else:
            cycle_duration = 2
        for i in range(cycle_duration):
            register_values[clock_cycle] = register_x
            if i == cycle_duration - 1:
                value = 0 if line == "noop" else int(line.split()[1])
                register_x += value
            clock_cycle += 1

    return sum(i * register_values[i] for i in range(20, 260, 40))


def solve_part_2():
    crt = []
    for cycle, register_value in register_values.items():
        crt.append('█' if abs((cycle - 1) % 40 - register_value) <= 1 else ' ')
    print("Part 2:")
    for i in range(0, len(crt), 40):
        print(''.join(crt[i:i + 40]))


def get_puzzle_input():
    return [x.strip() for x in open("input.txt")]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    solve_part_2()

