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


def main():
    password = solve_part1(INPUTS_FILE_PATH)
    print(f"The Password to open the door is: {password}")


if __name__ == "__main__":
    main()
