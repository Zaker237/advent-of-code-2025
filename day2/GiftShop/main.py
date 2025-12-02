from pathlib import Path

INPUTS_FILE_PATH = Path("inputs.txt")


def is_invalid_id_method1(value: int) -> bool:
    numbers_str = str(value)
    if len(numbers_str) % 2 != 0:
        return False
    middle = int(len(numbers_str) / 2)
    if middle == 1:
        first_part = "".join(numbers_str[0])
        second_part = "".join(numbers_str[1])
    else:
        first_part = "".join(numbers_str[:middle])
        second_part = "".join(numbers_str[middle:])
    return first_part == second_part


def is_invalid_id_method2(value: int) -> bool:
    numbers_str = str(value)
    middle = int(len(numbers_str) / 2)
    values = []
    if middle == 1:
        items = []
        for v in numbers_str:
            items.append(v)
        values.append(items)
    else:
        for pos_len in range(1, middle + 1):
            if len(numbers_str) % pos_len != 0:
                continue
            items = []
            for index in range(0, len(numbers_str), pos_len):
                if index == 0:
                    val = numbers_str[:pos_len]
                else:
                    val = numbers_str[index : index + pos_len]
                items.append(val)
            if items:
                values.append(items)
    is_valid = False
    for elems in values:
        values_bool = [item == elems[0] for item in elems]
        if all(values_bool):
            is_valid = True
    return is_valid


def handel_single_range_method1(s_range: str) -> list[int]:
    if "-" not in s_range or s_range.count("-") != 1:
        raise ValueError(f"'{s_range}' is not a valid range")

    result = []
    start = int(s_range.split("-")[0])
    end = int(s_range.split("-")[1])
    values = list(range(start, end + 1, 1))
    for value in values:
        if is_invalid_id_method1(value):
            result.append(value)
    return result


def handel_single_range_method2(s_range: str) -> list[int]:
    if "-" not in s_range or s_range.count("-") != 1:
        raise ValueError(f"'{s_range}' is not a valid range")

    result = []
    start = int(s_range.split("-")[0])
    end = int(s_range.split("-")[1])
    values = list(range(start, end + 1, 1))
    for value in values:
        if is_invalid_id_method2(value):
            result.append(value)
    return result


def solve_part1(file_path: Path) -> int:
    if not file_path.exists():
        raise FileNotFoundError()

    with open(file_path) as fp:
        file_lines = [item[:-1] for item in fp.readlines()]
    if not file_lines:
        raise Exception(f"the file {file_path.stem} do not contains id's ranges")
    ids = ",".join(file_lines)
    # ids = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    ids_list = ids.split(",")
    invalids_ids = []
    for id_range in ids_list:
        invalids_ids_in_range = handel_single_range_method1(id_range.strip())
        if invalids_ids_in_range:
            invalids_ids.extend(invalids_ids_in_range)
    return invalids_ids


def solve_part2(file_path: Path) -> int:
    if not file_path.exists():
        raise FileNotFoundError()

    with open(file_path) as fp:
        file_lines = [item[:-1] for item in fp.readlines()]
    if not file_lines:
        raise Exception(f"the file {file_path.stem} do not contains id's ranges")
    ids = ",".join(file_lines)
    # ids = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    ids_list = ids.split(",")
    invalids_ids = []
    for id_range in ids_list:
        invalids_ids_in_range = handel_single_range_method2(id_range.strip())
        if invalids_ids_in_range:
            invalids_ids.extend(invalids_ids_in_range)
    return invalids_ids


def main():
    invalid_ids1 = solve_part1(INPUTS_FILE_PATH)
    print(f"The Password to open the door is: {sum(invalid_ids1)}")
    invalid_ids2 = solve_part2(INPUTS_FILE_PATH)
    print(f"The Password to open the door is: {sum(invalid_ids2)}")


if __name__ == "__main__":
    main()
