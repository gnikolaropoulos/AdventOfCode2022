import re


def manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y):
    return abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)


def solve_part_1(input):
    empty_positions = set()
    for i, line in enumerate(input):
        distance = manhattan_distance(line[0], line[1], line[2], line[3])

        for x in range(line[0] - distance, line[0] + distance + 1):
            if x == line[2] and line[3] == 2000000:
                continue

            if manhattan_distance(line[0], line[1], x, 2000000) <= distance:
                empty_positions.add((x, 2000000))

    return len(empty_positions)


def solve_part_2(input):
    sensor_distances = {}

    for line in input:
        sensor_distances[(line[0], line[1])] = manhattan_distance(line[0], line[1], line[2], line[3])

    for y in range(0, 4000000 + 1):
        ranges = []
        for (sx, sy), distance in sensor_distances.items():
            distance_y = abs(sy - y)
            if distance > distance_y:
                distance_x = distance - distance_y
                ranges.append((max(0, sx - distance_x), min(4000000 + 1, sx + distance_x + 1)))

        ranges = sorted(ranges)
        distress_beacon_x = 0

        for i in range(1, len(ranges)):
            high = ranges[i - 1][1]
            low = ranges[i][0]
            distress_beacon_x = max(distress_beacon_x, high)
            if distress_beacon_x < low:
                return distress_beacon_x * 4000000 + y


def get_puzzle_input():
    coords = []
    with open("input.txt") as open_txt:
        for line in open_txt:
            coords.append([int(x) for x in re.findall(r'-?\d+', line.strip())])
    return coords


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
