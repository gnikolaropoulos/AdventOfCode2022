folder_sizes = {}


def solve_part_1(input):
    cmd_data = []
    i = 0
    while i < len(input):
        cmd = input[i][2:]
        if cmd.startswith('cd'):
            cmd_data.append((True, cmd[3:]))
            i += 1
        else:
            ls_content = []
            i += 1
            while i < len(input) and input[i][0] != '$':
                ls_content.append(input[i])
                i += 1
            cmd_data.append((False, ls_content))
    folder_structure = {}
    current_path = []
    for is_folder, data in cmd_data:
        if is_folder:
            if data == '..':
                current_path.pop()
            else:
                current_path.append(data)
        else:
            folder_structure[tuple(current_path)] = data

    for folder in folder_structure:
        folder_size(folder, folder_sizes, folder_structure)
    return sum(s for d, s in folder_sizes.items() if s <= 100_000)


def folder_size(folder, folder_sizes, folder_tree):
    if folder in folder_sizes:
        return folder_sizes[folder]
    size = 0
    for item in folder_tree[folder]:
        if item.startswith('dir '):
            size += folder_size(folder + (item[4:],), folder_sizes, folder_tree)
        else:
            size += int(item.split(' ')[0])
    folder_sizes[folder] = size
    return size


def solve_part_2():
    free_space = 70000000 - folder_sizes[('/',)]
    target = 30000000
    return min(size for _, size in folder_sizes.items() if free_space + size >= target)


def get_puzzle_input():
    return [x.strip() for x in open("input.txt")]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2()
    print(f"Part 2: {answer_2}")