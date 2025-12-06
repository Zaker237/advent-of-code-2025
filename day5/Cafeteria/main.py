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
    databases_items = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]
    worked_intervals = {}
    for line in databases_items:
        if not line or "-" not in line:
            continue
        did_interval_changed = False
        start_range = int(line.split("-")[0])
        end_range = int(line.split("-")[1])
        for interval in list(worked_intervals.keys()):
            # if the the interval is the same as the range
            start = int(interval.split("-")[0])
            end = int(interval.split("-")[1])
            if start_range >= start and end_range <= end:
                # the range is within the interval
                did_interval_changed = True
                break
            elif start_range <= start and end_range > start and end_range <= end:
                # create the 2 new rang
                did_interval_changed = True
                worked_intervals[f"{start_range}-{start - 1}"] = start - start_range
                break
            if start <= start_range and start_range < end and end <= end_range:
                # remove the old rage from the dict
                # create the 2 new rang
                did_interval_changed = True
                worked_intervals[f"{end - 1}-{end_range}"] = end_range - end
                break
        if not did_interval_changed:
            worked_intervals[line] = end_range - start_range + 1

    print(worked_intervals)
    return [a for a in worked_intervals.values() if a > 0]


def main():
    fresh_ingredients_1 = solve_part1(INPUTS_FILE_PATH)
    print(f"Ihe total fresh_ingredients is: {len(fresh_ingredients_1)}")
    fresh_ingredients_2 = solve_part2(INPUTS_FILE_PATH)
    print(f"Ihe total fresh_ingredients with method2 is: {sum(fresh_ingredients_2)}")


if __name__ == "__main__":
    main()
