from pathlib import Path

INPUTS_FILE_PATH = Path("inputs.txt")


def solve_part1(file_path: Path) -> int:
    if not file_path.exists():
        raise FileNotFoundError()

    with open(file_path) as fp:
        rotations = [item[:-1] for item in fp.readlines()]
    if not rotations:
        raise Exception(f"the file {file_path.stem} do not contains rotations")
    # rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    actual_position = 50
    password = 0
    for rotation in rotations:
        direction = rotation[0]
        num_move = int("".join(rotation[1:]))

        if direction.upper() not in ["R", "L"]:
            print(rotation)
            raise ValueError()
        if direction.upper() == "R":
            actual_position = (actual_position + num_move) % 100
        else:
            actual_position = (actual_position - num_move) % 100
        if actual_position == 0:
            password += 1
    return password


def solve_part2(file_path: Path) -> int:
    if not file_path.exists():
        raise FileNotFoundError()

    with open(file_path) as fp:
        rotations = [item[:-1] for item in fp.readlines()]
    if not rotations:
        raise Exception(f"the file {file_path.stem} do not contains rotations")
    # rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    actual_position = 50
    password = 0
    for rotation in rotations:
        print(rotation)
        direction = rotation[0]
        num_move = int("".join(rotation[1:]))
        if direction.upper() not in ["R", "L"]:
            print(rotation)
            raise ValueError()
        for _ in range(num_move):
            if direction.upper() == "R":
                actual_position += 1
            else:
                actual_position -= 1
            actual_position = actual_position % 100
            if actual_position == 0:
                password += 1
    return password


def main():
    password_method1 = solve_part1(INPUTS_FILE_PATH)
    password_method2 = solve_part2(INPUTS_FILE_PATH)
    print(f"The Password to open the door is: {password_method1}")
    print(
        f"The Password to open the door(Using method 0x434C49434B) is: {password_method2}"
    )


if __name__ == "__main__":
    main()
