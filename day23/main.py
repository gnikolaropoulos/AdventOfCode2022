from collections import defaultdict


def try_move(row, column, position, direction):
    if direction == 0:
        if all((x, y) not in position for x, y in [(row - 1, column - 1), (row - 1, column), (row - 1, column + 1)]):
            return True, (row - 1, column)
    if direction == 1:
        if all((x, y) not in position for x, y in [(row + 1, column - 1), (row + 1, column), (row + 1, column + 1)]):
            return True, (row + 1, column)
    if direction == 2:
        if all((x, y) not in position for x, y in [(row - 1, column - 1), (row, column - 1), (row + 1, column - 1)]):
            return True, (row, column - 1)
    if direction == 3:
        if all((x, y) not in position for x, y in [(row - 1, column + 1), (row, column + 1), (row + 1, column + 1)]):
            return True, (row, column + 1)
    return False, None


def get_neighbours_coords(row, column):
    neighbours = []
    for row_index in range(row - 1, row + 2):
        for column_index in range(column - 1, column + 2):
            if (row_index, column_index) != (row, column):
                neighbours.append((row_index, column_index))
    return neighbours


def play_round(positions, round_no):
    proposals = defaultdict(list)
    for row, column in positions:
        ok = True
        for rr, cc in get_neighbours_coords(row, column):
            if (rr, cc) in positions:
                ok = False
        if ok:
            proposals[row, column].append((row, column))
            continue
        for direction in range(4):
            ok, destination = try_move(row, column, positions, (round_no + direction) % 4)
            if ok:
                proposals[destination].append((row, column))
                break
        if not ok:
            proposals[row, column].append((row, column))

    end_positions = set()
    moved = False
    for destination, starts in proposals.items():
        if len(starts) == 1:
            end_positions.add(destination)
            moved = moved or (destination != starts[0])
        else:
            for p in starts:
                end_positions.add(p)
    return end_positions, moved


def get_puzzle_input():
    lns = [x.strip() for x in open('input.txt')]
    positions = set()
    for row, line in enumerate(lns):
        for column, character in enumerate(line):
            if character == '#':
                positions.add((row, column))
    return positions


def solve_part_1(input):
    for i in range(10):
        pos, _ = play_round(input, i)

    min_x = min(input)[0]
    min_y = min(input, key=lambda c: c[1])[1]
    max_x = max(input)[0]
    max_y = max(input, key=lambda c: c[1])[1]
    dx = max_x - min_x + 1
    dy = max_y - min_y + 1
    return dx * dy - len(input)


def solve_part_2(input):
    i = 0
    moved = True
    while moved:
        input, moved = play_round(input, i)
        i += 1
    return i


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
