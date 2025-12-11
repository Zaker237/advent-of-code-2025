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


def find_start_postion(data: list[list[str]]):
    pos_x, pos_y = None, None
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                pos_x = i + 1
                pos_y = j
    return pos_x, pos_y


def solve_part1(file_path: Path) -> list[int]:
    lines = read_file_lines(file_path)
    if not lines:
        raise Exception(f"the file {file_path.stem} do not contains sheets data")
    # lines = [
    #     ".......S.......",
    #     "...............",
    #     ".......^.......",
    #     "...............",
    #     "......^.^......",
    #     "...............",
    #     ".....^.^.^.....",
    #     "...............",
    #     "....^.^...^....",
    #     "...............",
    #     "...^.^...^.^...",
    #     "...............",
    #     "..^...^.....^..",
    #     "...............",
    #     ".^.^.^.^.^...^.",
    #     "...............",
    # ]
    datas = [list(a) for a in lines]
    result = 0
    start_x, start_y = find_start_postion(datas)
    if start_x is None or start_y is None:
        raise ValueError("Starting point not found")
    positions = [start_y]
    for i in range(start_x, len(datas)):
        new_positions = []
        for j in range(len(datas[i])):
            if j in positions:
                datas[i][j] = "|"
                #            else:
                if i + 1 < len(datas) and datas[i + 1][j] == "^":
                    result += 1
                    if j + 1 < len(datas[i]):
                        new_positions.append(j + 1)
                    if j > 0:
                        new_positions.append(j - 1)
                else:
                    new_positions.append(j)
        positions = [a for a in new_positions]
        # print("\n".join(["".join(line) for line in datas]))
        # print("\n\n")

    return result


def solve_part2(file_path: Path) -> list[int]:
    result = 0
    return result


def main():
    total = solve_part1(INPUTS_FILE_PATH)
    print(f"The Amount of times will the beam be split is: {total}")
    total_2 = solve_part2(INPUTS_FILE_PATH)
    print(f"The Amount of times will the beam be split with method2 is: {total_2}")


if __name__ == "__main__":
    main()
