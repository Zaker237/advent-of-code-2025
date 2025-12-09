from pathlib import Path

INPUTS_FILE_PATH = Path("inputs.txt")


def read_file_lines(file_path: Path) -> list[str]:
    if not file_path.exists():
        raise FileNotFoundError()

    with open(file_path) as fp:
        file_lines = [
            item[:-1]
            for item in fp.readlines()
            if len(item) > 0 and item.endswith("\n") and item != "\n"
        ]
    return file_lines


def get_adjacent_cells(grid, x_coord, y_coord):
    result = {}
    for x, y in [
        (x_coord + i, y_coord + j)
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        if i != 0 or j != 0
    ]:
        if (x, y) in grid.cells:
            result[(x, y)] = grid.cells[(x, y)]


def handel_single_position(data: list[list[str]], i: int, j: int) -> list[str]:
    return [
        data[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else None,
        data[i - 1][j] if i - 1 >= 0 else None,
        data[i - 1][j + 1] if i - 1 >= 0 and j + 1 <= len(data[i]) - 1 else None,
        data[i][j - 1] if j - 1 >= 0 else None,
        data[i][j + 1] if j + 1 <= len(data[i]) - 1 else None,
        data[i + 1][j - 1] if i + 1 <= len(data) - 1 and j - 1 >= 0 else None,
        data[i + 1][j] if i + 1 <= len(data) - 1 else None,
        data[i + 1][j + 1]
        if i + 1 <= len(data) - 1 and j + 1 <= len(data[i]) - 1
        else None,
    ]


def solve_part1(file_path: Path) -> list[int]:
    papers = read_file_lines(file_path)
    if not papers:
        raise Exception(f"the file {file_path.stem} do not contains papers")
    # papers = [
    #     "..@@.@@@@.",
    #     "@@@.@.@.@@",
    #     "@@@@@.@.@@",
    #     "@.@@@@..@.",
    #     "@@.@@@@.@@",
    #     ".@@@@@@@.@",
    #     ".@.@.@.@@@",
    #     "@.@@@.@@@@",
    #     ".@@@@@@@@.",
    #     "@.@.@@@.@.",
    # ]

    datas = [[a for a in item] for item in papers]

    results = []
    for i in range(len(datas)):
        for j in range(len(datas[i])):
            rolls = handel_single_position(datas, i, j)
            rolls_filtered = [val for val in rolls if val and val == "@"]
            if datas[i][j] == "@" and len(rolls_filtered) < 4:
                results.append((i, j))
    return results


def solve_part2(file_path: Path) -> list[int]:
    papers = read_file_lines(file_path)
    if not papers:
        raise Exception(f"the file {file_path.stem} do not contains papers")
    # papers = [
    #     "..@@.@@@@.",
    #     "@@@.@.@.@@",
    #     "@@@@@.@.@@",
    #     "@.@@@@..@.",
    #     "@@.@@@@.@@",
    #     ".@@@@@@@.@",
    #     ".@.@.@.@@@",
    #     "@.@@@.@@@@",
    #     ".@@@@@@@@.",
    #     "@.@.@@@.@.",
    # ]

    datas = [[a for a in item] for item in papers]

    results = []
    is_roll_removed = True
    removed_rolls = None
    while is_roll_removed:
        removable = []
        print(
            f"Remove {removed_rolls} rolls of paper:"
            if removed_rolls
            else "Initial state:"
        )
        # print("\n".join([str(elem) for elem in datas]))
        for i in range(len(datas)):
            for j in range(len(datas[i])):
                rolls = handel_single_position(datas, i, j)
                rolls_filtered = [val for val in rolls if val and val == "@"]
                if datas[i][j] == "@" and len(rolls_filtered) < 4:
                    results.append((i, j))
                    removable.append((i, j))
        if len(removable) > 0:
            removed_rolls = len(removable)
            for a, b in removable:
                datas[a][b] = "."
            removable = []
        else:
            is_roll_removed = False
    return results


def main():
    rolls = solve_part1(INPUTS_FILE_PATH)
    print(f"The total of rolls of paper that can be removed is: \n{len(rolls)}")
    rolls_2 = solve_part2(INPUTS_FILE_PATH)
    print(
        f"The total output rolls of paper that can be removed with method2 is: {len(rolls_2)}"
    )


if __name__ == "__main__":
    main()
