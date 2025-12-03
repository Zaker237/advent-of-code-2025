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


def handel_single_batterie(batterie: str) -> int:
    digits = [int(batterie[val]) for val in range(len(batterie))]
    first_digit = max(digits[:-1])
    first_digit_pos = digits.index(first_digit)
    second_digit = max(digits[first_digit_pos + 1 :])

    return int(f"{first_digit}{second_digit}")


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
        joltage = handel_single_batterie(batterie)
        if joltage:
            results.append(joltage)
    return results


def main():
    joltages = solve_part1(INPUTS_FILE_PATH)
    print(f"Ihe total output joltage is: {sum(joltages)}")


if __name__ == "__main__":
    main()
