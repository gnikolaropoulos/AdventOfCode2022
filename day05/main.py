stacks = [['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V'],
          ['D', 'Q', 'L'],
          ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B'],
          ['L', 'C', 'D', 'H', 'B', 'Q', 'G'],
          ['V', 'G', 'L', 'F', 'Z', 'S'],
          ['D', 'G', 'N', 'P'],
          ['D', 'Z', 'P', 'V', 'F', 'C', 'W'],
          ['C', 'P', 'D', 'M', 'S'],
          ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C']]


def solve_part_1(input):
    result = ''
    for count, from_stack, to_stack in input:
        from_stack -= 1
        to_stack -= 1
        for _ in range(count):
            item = stacks[from_stack].pop()
            stacks[to_stack].append(item)

    for stack in stacks:
        result += stack[-1]

    return result


def solve_part_2(input):
    result = ''
    for count, from_stack, to_stack in input:
        from_stack -= 1
        to_stack -= 1
        items = stacks[from_stack][-count:]
        stacks[from_stack] = stacks[from_stack][:-count]
        stacks[to_stack].extend(items)

    for stack in stacks:
        result += stack[-1]

    return result


def get_puzzle_input():
    moves = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            if line.startswith('move'):
                numbers = line.split(' ')
                moves.append(list(map(int, numbers[1::2])))
    return moves


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")