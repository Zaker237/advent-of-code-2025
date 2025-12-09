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


def transpose_strings(strings):
    grid = [list(row) for row in strings]
    # Determine max width to pad all rows equally
    max_len = max(len(row) for row in grid)

    for row in grid:
        row.extend(" " * (max_len - len(row)))

    transposed = ["".join(grid[r][c] for r in range(len(grid))) for c in range(max_len)]

    return transposed


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
    sheets = read_file_lines(file_path)
    if not sheets:
        raise Exception(f"the file {file_path.stem} do not contains sheets data")
    # sheets = [
    #     "123 328  51 64 ",
    #     " 45 64  387 23 ",
    #     "  6 98  215 314",
    #     "*   +   *   +  ",
    # ]
    symbols = [val for val in sheets[-1].split(" ") if val and val != " "]
    operations = {
        str(index): {"operator": symbol, "values": []}
        for index, symbol in enumerate(symbols, 1)
    }
    symbol_sheet = sheets[-1]
    for line in sheets[:-1]:
        values = [val for val in line.split(" ") if val and val != " "]
        if len(values) != len(symbols):
            continue
        for idx, item in enumerate(values, 1):
            operations[f"{idx}"]["values"].append(int(item))
    moves = []
    for key in operations:
        operations[key]["length"] = len(str(max(operations[key]["values"])))
        moves.append(len(str(max(operations[key]["values"]))))
    _operations = []
    result = 0
    for idx, line in enumerate(sheets[::-1]):
        reverted_line = line[::-1]
        if idx != 0:
            _operations.append(reverted_line)
    transposed_values = [val[::-1] for val in transpose_strings(_operations)]
    current_pos = 0
    final_operations = {}
    for pos, move in enumerate(moves[::-1], 1):
        values_block = transposed_values[current_pos : current_pos + move]
        symbol_block = symbol_sheet[::-1][current_pos : current_pos + move]
        current_pos += move + 1
        final_operations[str(pos)] = {
            "operator": symbol_block.strip(),
            "values": [int(item.strip()) for item in values_block],
        }
    result = 0
    for key in final_operations.keys():
        if final_operations[key]["operator"].strip() == "+":
            result += sum(final_operations[key]["values"])
        else:
            result += math.prod(final_operations[key]["values"])
    return result


def main():
    total = solve_part1(INPUTS_FILE_PATH)
    print(f"The grand total found: {total}")
    total_2 = solve_part2(INPUTS_FILE_PATH)
    print(f"The grand total found with method2 is: {total_2}")


if __name__ == "__main__":
    main()
