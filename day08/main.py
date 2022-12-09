def solve_part_1(input):
    rows = len(input)
    cols = len(input[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visible_trees = 0
    for i in range(rows):
        for j in range(cols):
            is_visible = False
            for direction in range(len(directions)):
                height = input[i][j]
                neighbor_heights = []
                next_i, next_j = i, j
                while 0 <= next_i < rows and 0 <= next_j < cols:
                    if (next_i, next_j) != (i, j):
                        neighbor_heights.append(input[next_i][next_j])
                    (next_i, next_j) = (next_i + directions[direction][0], next_j + directions[direction][1])
                if len(neighbor_heights) == 0 or max(neighbor_heights) < height:
                    is_visible = True
                    break
            if is_visible:
                visible_trees += 1
    return visible_trees


def solve_part_2(input):
    rows = len(input)
    cols = len(input[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    best_score = 0
    for i in range(rows):
        for j in range(cols):
            viewing_distances = []
            for direction in range(len(directions)):
                tree = input[i][j]
                next_i, next_j = i, j
                viewing_distance = 0
                while 0 <= next_i < rows and 0 <= next_j < cols:
                    if (next_i, next_j) != (i, j):
                        viewing_distance += 1
                        next_tree = input[next_i][next_j]
                        if next_tree >= tree:
                            break
                    (next_i, next_j) = (next_i + directions[direction][0], next_j + directions[direction][1])
                viewing_distances.append(viewing_distance)
            best_score = max(best_score, scenic_score(viewing_distances))
    return best_score


def scenic_score(list):
    result = 1
    for item in list:
        result *= item
    return result


def get_puzzle_input():
    grid = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            grid.append([int(height) for height in line.strip()])
    return grid


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")