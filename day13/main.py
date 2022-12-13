from functools import cmp_to_key


def solve_part_1(input):
    result = 0
    for index, (left, right) in enumerate(input):
        if compare(left, right) < 0:
            result += index + 1
    return result


def compare(left, right):
    is_list1_int = isinstance(left, int)
    is_list2_int = isinstance(right, int)
    if is_list1_int and is_list2_int:
        if left <right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    if is_list1_int:
        left = [left]
    if is_list2_int:
        right = [right]
    for new_left, new_right in zip(left, right):
        result = compare(new_left, new_right)
        if result != 0:
            return result
    result = len(left) - len(right)
    if result < 0:
        return -1
    elif result == 0:
        return 0
    else:
        return 1


def solve_part_2(input):
    input.extend([[[2]],[[6]]])
    packets = sorted(input, key=cmp_to_key(compare))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


def get_puzzle_input():
    packets = []
    with open('input.txt') as open_txt:
        for pair in open_txt.read().split('\n\n'):
            packets.append(list(map(eval, pair.split('\n'))))

    return packets


def get_puzzle_input2():
    packets = []
    with open('input.txt') as open_txt:
        for pair in open_txt.read().split('\n\n'):
            packets.extend((map(eval, pair.split('\n'))))

    return packets


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input2 = get_puzzle_input2()

    answer_2 = solve_part_2(puzzle_input2)
    print(f"Part 2: {answer_2}")
