# from collections import
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


def solve_part1(file_path: Path) -> list[int]:
    databases_items = read_file_lines(file_path)
    if not databases_items:
        raise Exception(f"the file {file_path.stem} do not contains databases_items")
    # databases_items = [
    #     "3-5",
    #     "10-14",
    #     "16-20",
    #     "12-18",
    #     "",
    #     "1",
    #     "5",
    #     "8",
    #     "11",
    #     "17",
    #     "32",
    # ]
    ingredient_ids = []
    ranges = []
    fresh_ingredient_ids = []
    for line in databases_items:
        if not line:
            continue
        if "-" in line:
            ranges.append(line)
        else:
            ingredient_ids.append(int(line))

    for ingredient in ingredient_ids:
        for interval in ranges:
            start = int(interval.split("-")[0])
            end = int(interval.split("-")[1])
            if ingredient >= start and ingredient <= end:
                if ingredient not in fresh_ingredient_ids:
                    fresh_ingredient_ids.append(ingredient)
    # print(fresh_ingredient_ids)
    return fresh_ingredient_ids


def solve_part2(file_path: Path) -> list[int]:
    databases_items = read_file_lines(file_path)
    if not databases_items:
        raise Exception(f"the file {file_path.stem} do not contains databases_items")
    # databases_items = [
    #     "3-5",
    #     "10-14",
    #     "16-20",
    #     "12-18",
    #     "",
    #     "1",
    #     "5",
    #     "8",
    #     "11",
    #     "17",
    #     "32",
    # ]
    ranges = []
    for line in databases_items:
        if not line or "-" not in line:
            continue
        a, b = int(line.split("-")[0]), int(line.split("-")[1])
        ranges.append((a, b))

    ranges.sort()

    worked_intervals = []
    cur_start, cur_end = ranges[0]
    # print(ranges)
    for start, end in ranges[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            worked_intervals.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    worked_intervals.append((cur_start, cur_end))
    # print(worked_intervals)

    return [(b - a + 1) for a, b in worked_intervals]


def main():
    fresh_ingredients_1 = solve_part1(INPUTS_FILE_PATH)
    print(f"Ihe total fresh_ingredients is: {len(fresh_ingredients_1)}")
    fresh_ingredients_2 = solve_part2(INPUTS_FILE_PATH)
    print(f"Ihe total fresh_ingredients with method2 is: {sum(fresh_ingredients_2)}")


if __name__ == "__main__":
    main()
