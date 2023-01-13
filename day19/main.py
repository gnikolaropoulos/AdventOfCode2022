MATERIALS = {
    'ore': 0,
    'clay': 1,
    'obsidian': 2,
    'geode': 3,
}


def parse_robot(element):
    cost = element.split('costs')[1]
    material_costs = [0]*3
    for x in cost.split('and'):
        cnt, kind = x.strip().split()
        material_code = MATERIALS[kind]
        material_costs[material_code] = int(cnt)
    return material_costs


def get_puzzle_input():
    blueprints = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            materials = line.split(': ')[1].split('.')
            blueprint = [
                parse_robot(material) for material in materials[:4]
            ]
            blueprints.append(blueprint)
        return blueprints


def add(robots, material):
    return tuple([r + m for r, m in zip(robots, material)])

def sub(mat, cost):
    return tuple(m - c for m, c in zip(mat, cost))

def inc(robots, i):
    robots_list = list(robots)
    robots_list[i] += 1
    return tuple(robots_list)


def solve(blueprint, minutes):
    states = {}

    def opt(ra, rb, rc, rd, ma, mb, mc, t):
        if t <= 0: return 0
        state = ra, rb, rc, rd, ma, mb, mc, t
        if state in states:
            return states[state]
        best = 0
        geo = rd
        robots = ra, rb, rc, rd
        materials = ma, mb, mc
        for i in range(4)[::-1]:
            mat2 = sub(materials, blueprint[i])
            if min(mat2) >= 0:
                ra2, rb2, rc2, rd2 = inc(robots, i)
                ma2, mb2, mc2 = add(robots, mat2)
                best = max(best,
                    geo + opt(ra2, rb2, rc2, rd2, ma2, mb2, mc2, t - 1)
                )
                if i >= 2:
                    states[state] = best
                    return best
        ma2, mb2, mc2 = add(robots, materials)
        best = max(best, geo + opt(ra, rb, rc, rd, ma2, mb2, mc2, t - 1))
        states[state] = best
        return best

    return opt(1, 0, 0, 0, 0, 0, 0, minutes)



def solve_part_1(input):
    result = 0
    for i, blueprint in list(enumerate(input)):
        sc = solve(blueprint, 24)
        result += (i+1)*sc
    return result

def solve_part_2(input):
    result = 1
    for i, blueprint in list(enumerate(input))[:3]:
        score = solve(blueprint, 32)
        result *= score
    return result

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")