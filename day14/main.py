def solve_part_1(input, lower_end):
    current_position = (500, 0)
    units_of_sand = 0
    while True:
        if current_position[1] > lower_end:
            return units_of_sand
        if not input.__contains__((current_position[0], current_position[1] + 1)):
            current_position = (current_position[0], current_position[1] + 1)
        elif not input.__contains__((current_position[0] - 1, current_position[1] + 1)):
            current_position = (current_position[0] - 1, current_position[1] + 1)
        elif not input.__contains__((current_position[0] + 1, current_position[1] + 1)):
            current_position = (current_position[0] + 1, current_position[1] + 1)
        else:
            units_of_sand += 1
            input.add(current_position)
            current_position = (500, 0)


def solve_part_2(input, lower_end):
    lower_end += 2
    for i in range(-500, 1500):
        input.add((i, lower_end))

    current_position = (500, 0)
    units_of_sand = 0
    while True:
        if not input.__contains__((current_position[0], current_position[1] + 1)):
            current_position = (current_position[0], current_position[1] + 1)
        elif not input.__contains__((current_position[0] - 1, current_position[1] + 1)):
            current_position = (current_position[0] - 1, current_position[1] + 1)
        elif not input.__contains__((current_position[0] + 1, current_position[1] + 1)):
            current_position = (current_position[0] + 1, current_position[1] + 1)
        else:
            units_of_sand += 1
            if current_position[0] == 500 and current_position[1] == 0:
                return units_of_sand
            input.add(current_position)
            current_position = (500, 0)


def get_puzzle_input():
    grid = set()
    lower_end = 0
    with open('input.txt') as open_txt:
        for line in open_txt:
            draw_lines = line.strip().split("->")
            start_row = None
            start_col = None
            for draw_line in draw_lines:
                if start_row is None:
                    start_row = int(draw_line.strip().split(",")[0])
                    start_col = int(draw_line.strip().split(",")[1])
                    if start_col > lower_end:
                        lower_end = start_col
                    continue
                end_row = int(draw_line.strip().split(",")[0])
                end_col = int(draw_line.strip().split(",")[1])
                if end_col > lower_end:
                    lower_end = end_col
                if start_row == end_row:
                    if start_col < end_col:
                        for i in range(start_col, end_col + 1):
                            grid.add((start_row, i))
                    else:
                        for i in range(end_col, start_col + 1):
                            grid.add((start_row, i))
                elif start_col == end_col:
                    if start_row < end_row:
                        for i in range(start_row, end_row + 1):
                            grid.add((i, start_col))
                    else:
                        for i in range(end_row, start_row + 1):
                            grid.add((i, start_col))
                start_row = end_row
                start_col = end_col
    return grid, lower_end


if __name__ == "__main__":
    puzzle_input, lower_end = get_puzzle_input()
    answer_1 = solve_part_1(puzzle_input, lower_end)
    print(f"Part 1: {answer_1}")

    puzzle_input, lower_end = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input, lower_end)
    print(f"Part 2: {answer_2}")
