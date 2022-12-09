from itertools import product

DIRECTIONS = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}


def solve_part_1(input):
    head = (0, 0)
    tail = (0, 0)

    visited = set()
    visited.add(tail)

    for command in input:
        direction, steps = command.split(" ")
        steps = int(steps)
        d = DIRECTIONS[direction]
        for _ in range(steps):
            head = (head[0] + d[0], head[1] + d[1])
            tail = move_tail(head, tail)
            visited.add(tail)

    return len(visited)


def solve_part_2(input):
    head = (0, 0)
    knots = [(0, 0)] * 10
    visited = set()
    visited.add(head)

    for command in input:
        direction, steps = command.split(" ")
        steps = int(steps)
        direction = DIRECTIONS[direction]
        for _ in range(steps):
            knots[0] = (knots[0][0] + direction[0], knots[0][1] + direction[1])
            for i in range(9):
                i += 1
                head = knots[i - 1]
                tail = knots[i]
                tail = move_tail(head, tail)
                knots[i] = tail
            visited.add(knots[-1])
    return len(visited)


def move_tail(head, tail):
    if head == (tail[0] - 2, tail[1]):
        tail = (tail[0] - 1, tail[1])
    elif head == (tail[0] + 2, tail[1]):
        tail = (tail[0] + 1, tail[1])
    elif head == (tail[0], tail[1] - 2):
        tail = (tail[0], tail[1] - 1)
    elif head == (tail[0], tail[1] + 2):
        tail = (tail[0], tail[1] + 1)
    elif not are_neighbours(head, tail):
        dx = 1 if head[0] > tail[0] else -1
        dy = 1 if head[1] > tail[1] else -1
        tail = (tail[0] + dx, tail[1] + dy)
    return tail


def are_neighbours(head, tail):
    for dx, dy in product((-1, 0, 1), repeat=2):
        if head == (tail[0] + dx, tail[1] + dy):
            return True
    return False


def get_puzzle_input():
    return [x.strip() for x in open("input.txt")]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
