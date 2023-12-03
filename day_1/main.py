import re

# Ensures specific cases like "twoone" map to 21 (so as to get all possible digits)
DIGIT_MAP = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def process_number_names(raw_string: str) -> str:
    for k, v in DIGIT_MAP.items():
        raw_string = raw_string.replace(k, v)

    return raw_string


def get_calibration_value(dirty_string: str) -> int:
    found = re.findall(r"\d", dirty_string)
    number_string = found[0] + found[-1]
    return int(number_string)


if __name__ == "__main__":
    calibration_sum = 0

    with open("debug_2.txt", "r", encoding="UTF-8") as file:
        while line := file.readline():
            processed_line = process_number_names(line.rstrip())
            calibration_sum += get_calibration_value(processed_line)

    print(f"Sum of all processed calibration values = {calibration_sum}")
