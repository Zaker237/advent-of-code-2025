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


def find_max_digit(value: str, MAX=1) -> tuple[int, int]:
    if MAX == 0:
        digits = [int(value[val]) for val in range(len(value))]
    else:
        digits = [int(value[:MAX][val]) for val in range(len(value[:MAX]))]
    first_digit = max(digits)
    first_digit_pos = digits.index(first_digit)
    return first_digit, first_digit_pos


def handel_single_batterie_method1(batterie: str) -> int:
    digits = [int(batterie[val]) for val in range(len(batterie))]
    first_digit, first_digit_pos = find_max_digit(batterie, -1)
    second_digit = max(digits[first_digit_pos + 1 :])

    return int(f"{first_digit}{second_digit}")


def handel_single_batterie_method2(batterie: str, joltage_length: int = 1) -> int:
    result = ""
    actual_pos = 0
    for i in range(joltage_length - 1, 0, -1):
        first_digit, first_digit_pos = find_max_digit(batterie[actual_pos:], -i)
        result = f"{result}{first_digit}"
        actual_pos += first_digit_pos + 1
    first_digit, first_digit_pos = find_max_digit(batterie[actual_pos:], None)
    result = f"{result}{first_digit}"

    return int(result)


def solve_part1(file_path: Path) -> list[int]:
    batteries = read_file_lines(file_path)
    if not batteries:
        raise Exception(f"the file {file_path.stem} do not contains batteries")
    # batteries = [
    #     "987654321111111",
    #     "811111111111119",
    #     "234234234234278",
    #     "818181911112111",
    # ]
    results = []
    for batterie in batteries:
        joltage = handel_single_batterie_method1(batterie)
        if joltage:
            results.append(joltage)
    return results


def solve_part2(file_path: Path, joltage_length: int = 1) -> list[int]:
    batteries = read_file_lines(file_path)
    if not batteries:
        raise Exception(f"the file {file_path.stem} do not contains batteries")
    # batteries = [
    #    "987654321111111",
    #    "811111111111119",
    #    "234234234234278",
    #    "818181911112111",
    # ]
    results = []
    for batterie in batteries:
        joltage = handel_single_batterie_method2(batterie, joltage_length)
        if joltage:
            results.append(joltage)
    return results


def main():
    joltages_1 = solve_part1(INPUTS_FILE_PATH)
    print(f"The total output joltage is: {sum(joltages_1)}")
    joltages_2 = solve_part2(INPUTS_FILE_PATH, 12)
    print(f"The total output joltage with method2 is: {sum(joltages_2)}")


if __name__ == "__main__":
    main()
