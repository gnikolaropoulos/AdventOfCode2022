
part1_combined_scores = [[4, 8, 3],
                         [1, 5, 9],
                         [7, 2, 6]]

part2_combined_scores = [[3, 4, 8],
                         [1, 5, 9],
                         [2, 6, 7]]

letterToIndexMapping = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}

def solve_part_1(input):
    total_score = 0
    for line in input:
        choices = line.split(" ")
        total_score += part1_combined_scores[letterToIndexMapping.get(choices[0])][letterToIndexMapping.get(choices[1])]
    return total_score


def solve_part_2(input):
    total_score = 0
    for line in input:
        choices = line.split(" ")
        total_score += part2_combined_scores[letterToIndexMapping.get(choices[0])][letterToIndexMapping.get(choices[1])]
    return total_score


def get_puzzle_input():
    return [x.strip() for x in open('input.txt')]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")