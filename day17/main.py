ROCKS = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]


def move(dx, dy, x, y, rock, grid):
    x2, y2 = x + dx, y + dy
    for ddx, ddy in rock:
        if (x2 + ddx, y2 + ddy) in grid:
            return 0, 0
    return dx, dy


def play(rock, grid, max_height, actions, next_move):
    x, y = 3, max_height + 4
    while True:
        dx, dy = move(actions[next_move % len(actions)], 0, x, y, rock, grid)
        next_move += 1
        x, y = x + dx, y + dy

        dx, dy = move(0, -1, x, y, rock, grid)
        if dy == 0:
            break
        x, y = x + dx, y + dy

    for dx, dy in rock:
        grid.add((x + dx, y + dy))
        max_height = max(max_height, y + dy)
    return max_height, next_move


def solve_part_1(input):
    grid, max_height = init_grid()
    next_move = 0
    for i in range(2022):
        rock = ROCKS[i % len(ROCKS)]
        max_height, next_move = play(rock, grid, max_height, input, next_move)
    return max_height


def solve_part_2(input):
    grid, max_height = init_grid()
    states = {}
    repeat = 5
    heights = []
    i = 0
    next_action = 0
    while True:
        current_state = i % len(ROCKS), next_action % len(input)
        if current_state in states:
            repeat -= 1
            if repeat < 0:
                break
        states[current_state] = i, max_height
        heights.append(max_height)
        rock = ROCKS[i % len(ROCKS)]
        max_height, next_action = play(rock, grid, max_height, input, next_action)
        i += 1
    (current_step, current_height), (last_state_step, last_state_max_height) = (i, max_height), states[current_state]
    ds = current_step - last_state_step
    dh = current_height - last_state_max_height
    total_rocks = 1000000000000
    remaining_rocks = total_rocks - current_step
    laps = remaining_rocks // ds
    left = remaining_rocks % ds
    total_height = current_height + laps * dh
    extra_height = heights[last_state_step + left] - last_state_max_height
    return total_height + extra_height


def init_grid():
    grid = set()
    for i in range(9):
        grid.add((i, 0))
    for i in range(1000000):
        grid.add((0, i))
        grid.add((8, i))
    max_height = 0
    return grid, max_height


def get_puzzle_input():
    with open("input.txt") as open_txt:
        line = open_txt.readline().strip()
        arrows = [ch.strip() for ch in line]
        return [-1 if ch == '<' else 1 for ch in arrows]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
