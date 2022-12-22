DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(grid, start, end):
    queue = [(0, start)]
    visited = set()
    while queue:
        dist, (x, y) = queue.pop(0)
        if (x, y) == end:
            return dist
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in DIRECTIONS:
            if (
                    0 <= x + dx < len(grid)
                    and 0 <= y + dy < len(grid[0])
                    and ord(grid[x + dx][y + dy]) - ord(grid[x][y]) <= 1
            ):
                queue.append((dist + 1, (x + dx, y + dy)))

    return float("inf")


def solve_part_1(input):
    return bfs(puzzle_input[0], puzzle_input[1], puzzle_input[2])


def solve_part_2(input):
    grid, start, end, locations_of_a = puzzle_input
    distances_of_a = [bfs(grid, a, end) for a in locations_of_a]
    return min(distances_of_a)


def get_puzzle_input():
    grid = []
    start = (0, 0)
    end = (0, 0)
    locations_of_a = []
    with open("input.txt") as input_txt:
        line_index = 0
        for line in input_txt:
            grid.append(list(line.strip()))
            for index, char in enumerate(line.strip()):
                if char == "S":
                    start = (line_index, index)
                    locations_of_a.append((line_index, index))
                    grid[line_index][index] = "a"
                elif char == "E":
                    end = (line_index, index)
                    grid[line_index][index] = "z"
                elif char == "a":  # add a's to a list to loop over
                    locations_of_a.append((line_index, index))
            line_index += 1

    return grid, start, end, locations_of_a


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
