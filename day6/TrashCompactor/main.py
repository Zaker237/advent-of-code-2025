import math
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
    sheets = read_file_lines(file_path)
    if not sheets:
        raise Exception(f"the file {file_path.stem} do not contains sheets data")
    # sheets = [
    #     "123 328  51 64",
    #     "45 64  387 23 ",
    #     "6 98  215 314",
    #     "*   +   *   +",
    # ]
    symbols = [val for val in sheets[-1].split(" ") if val and val != " "]
    operations = {
        str(index): {"operator": symbol, "values": []}
        for index, symbol in enumerate(symbols, 1)
    }
    for line in sheets[:-1]:
        values = [val for val in line.split(" ") if val and val != " "]
        if len(values) != len(symbols):
            continue
        for idx, item in enumerate(values, 1):
            operations[f"{idx}"]["values"].append(int(item))
    result = 0
    for key in operations.keys():
        if operations[key]["operator"].strip() == "+":
            result += sum(operations[key]["values"])
        else:
            result += math.prod(operations[key]["values"])
    return result


def solve_part2(file_path: Path) -> list[int]:
    return 0


def main():
    total = solve_part1(INPUTS_FILE_PATH)
    print(f"The grand total found: {total}")
    total_2 = solve_part2(INPUTS_FILE_PATH)
    print(f"The grand total found with method2 is: {total_2}")


if __name__ == "__main__":
    main()
