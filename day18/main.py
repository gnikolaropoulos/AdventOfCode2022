def get_neighbours(x, y, z):
    return [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]


def get_faces(x, y, z):
    return [
        (x - 0.5, y, z),
        (x + 0.5, y, z),
        (x, y - 0.5, z),
        (x, y + 0.5, z),
        (x, y, z - 0.5),
        (x, y, z + 0.5),
    ]

def solve_part_1(input):
    surface_area = 0
    for x, y, z in input:
        for cube in get_neighbours(x, y, z):
            if cube not in input:
                surface_area += 1
    return surface_area


def solve_part_2(input):
    min_x = min_y = min_z = 0
    max_x = max_y = max_z = 0

    for x, y, z in input:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)

    min_x -= 1
    min_y -= 1
    min_z -= 1

    max_x += 1
    max_y += 1
    max_z += 1

    queue = [(min_x, min_y, min_z)]
    external_cubes = {(min_x, min_y, min_z)}

    while queue:
        x, y, z = queue.pop(0)
        for neighbor_x, neighbor_y, neighbor_z in get_neighbours(x, y, z):
            if not (min_x <= neighbor_x <= max_x and min_y <= neighbor_y <= max_y and min_z <= neighbor_z <= max_z):
                continue
            if (neighbor_x, neighbor_y, neighbor_z) in external_cubes or (neighbor_x, neighbor_y, neighbor_z) in input:
                continue

            queue.append((neighbor_x, neighbor_y, neighbor_z))
            external_cubes.add((neighbor_x, neighbor_y, neighbor_z))

    exterior_faces = set()
    for x, y, z in external_cubes:
        exterior_faces.update(get_faces(x, y, z))

    droplet_faces = set()
    for x, y, z in input:
        droplet_faces.update(get_faces(x, y, z))

    total = len(exterior_faces.intersection(droplet_faces))

    return total


def get_puzzle_input():
    cube_coords = []
    with open('input.txt') as open_txt:
        for line in open_txt:
            cube_coords.append(tuple(map(int, line.strip().split(','))))
    return cube_coords


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
