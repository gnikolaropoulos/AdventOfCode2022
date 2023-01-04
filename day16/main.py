import re

RATE = re.compile(r'rate=(\d+);')
VALVES = re.compile(r'to valves? (.*)$')


def solve_part_1(input):
    valves_pressures, valves_graph = input
    possible_paths = {}
    return solve(30, 'AA', frozenset(), possible_paths, valves_pressures, valves_graph)


def solve(duration, current_pipe, visited, paths, pressures, graph):
    if duration <= 0:
        return 0
    state = (duration, current_pipe, visited)
    if state in paths:
        return paths[state]
    score = 0
    if current_pipe not in visited and pressures[current_pipe] > 0:
        score = max(score, solve(duration - 1, current_pipe, visited.union({current_pipe}), paths, pressures, graph))
    for target in graph[current_pipe]:
        score = max(score, solve(duration - 1, target, visited, paths, pressures, graph))
    pressure = sum(pressures[v] for v in visited)
    paths[state] = pressure + score
    return paths[state]


def solve_part_2(input):
    pass


def get_puzzle_input():
    valve_pressures = {}
    valves_graph = {}
    with open("input.txt") as input_txt:
        for line in input_txt:
            valve = line.split()[1]
            pressure = int(RATE.search(line)[1])
            target_valves = VALVES.search(line)[1].split(", ")
            valve_pressures[valve] = pressure
            valves_graph[valve] = target_valves
    return valve_pressures, valves_graph


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
