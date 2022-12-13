import copy
import math


def solve_part_1(input):
    monkeys = copy.deepcopy(input)
    inspected_items_per_monkey = [0] * len(monkeys)
    for i in range(20):
        for monkey in range(len(monkeys)):
            for item in monkeys[monkey][0]:
                inspected_items_per_monkey[monkey] += 1
                new_value = apply_operation(monkeys[monkey][1], item)
                new_value = new_value // 3
                if new_value % monkeys[monkey][2] == 0:
                    monkey_to_place = monkeys[monkey][3]
                else:
                    monkey_to_place = monkeys[monkey][4]
                monkeys[monkey_to_place][0].append(new_value)
            monkeys[monkey][0] = []
    sorted_monkeys = sorted(inspected_items_per_monkey)
    return sorted_monkeys[-1] * sorted_monkeys[-2]


def apply_operation(operation, item):
    operation = operation.replace("old", str(item))
    if operation.__contains__("+"):
        return int(operation.split(" ")[0]) + int(operation.split(" ")[2])
    return int(operation.split(" ")[0]) * int(operation.split(" ")[2])


def solve_part_2(input):
    monkeys = copy.deepcopy(input)
    inspected_items_per_monkey = [0] * len(monkeys)
    normalization_factor = math.prod([monkeys[monkey][2] for monkey in monkeys])
    for i in range(10000):
        for monkey in range(len(monkeys)):
            for item in monkeys[monkey][0]:
                inspected_items_per_monkey[monkey] += 1
                new_value = apply_operation(monkeys[monkey][1], item)
                if new_value % monkeys[monkey][2] == 0:
                    monkey_to_place = monkeys[monkey][3]
                else:
                    monkey_to_place = monkeys[monkey][4]
                monkeys[monkey_to_place][0].append(new_value % normalization_factor)
            monkeys[monkey][0] = []
    sorted_monkeys = sorted(inspected_items_per_monkey)
    return sorted_monkeys[-1] * sorted_monkeys[-2]


def get_puzzle_input():
    monkeys = {}
    current_monkey = 0
    with open("input.txt") as input_txt:
        for line in input_txt:
            line = line.strip()
            if line.startswith("Monkey"):
                current_monkey = int(line.split(" ")[1][0])
                monkeys[current_monkey] = [[]]
                continue
            if line.startswith("Starting"):
                split = line.split(" ")
                values = split[2:]
                for value in values:
                    if value.__contains__(","):
                        monkeys[current_monkey][0].append(value.rstrip(","))
                    else:
                        monkeys[current_monkey][0].append(value)
                continue
            if line.startswith("Operation"):
                monkeys[current_monkey].append(line.split("=")[1].strip())
                continue
            if line.startswith("Test"):
                monkeys[current_monkey].append(int(line.split(" ")[-1]))
                continue
            if line.__contains__("true"):
                monkeys[current_monkey].append(int(line.split(" ")[-1]))
                continue
            if line.__contains__("false"):
                monkeys[current_monkey].append(int(line.split(" ")[-1]))
    return monkeys


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
