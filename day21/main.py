def get_puzzle_input():
    with open('input.txt') as f:
        monkeys = {}
        for l in f.read().split('\n'):
            monkey, expr = l.split(': ')
            monkeys[monkey] = expr.split(' ')
    return monkeys


def solve(monkeys, starting_monkey):
    expr = monkeys[starting_monkey]
    if len(expr) == 1:
        return int(expr[0])
    left, operator, right = expr
    solution_left, solution_right = solve(monkeys, left), solve(monkeys, right)
    result = int(solution_left + solution_right if operator == '+'
                 else solution_left - solution_right if operator == '-'
    else solution_left * solution_right if operator == '*'
    else solution_left / solution_right)
    return result


def solve_part_1(input):
    return solve(input, "root")


def solve_part_2(input):
    input["root"][1] = '-'
    answer = 0
    low = 1
    high = 10 ** 13
    while True:
        mid = (low + high) // 2
        input["humn"] = [str(mid)]
        solution = solve(input,"root")
        # print(f"mid {mid} = {z}")
        if solution == 0:
            answer = mid
            break
        elif solution < 0:
            high = mid
        elif solution > 0:
            low = mid
    return answer


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
