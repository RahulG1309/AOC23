import re
from typing import List


def calulate_num_matches(numbers_winning: List[str], numbers_have: List[str]):
    return len(set(numbers_winning).intersection(numbers_have))


def calculate_points(numbers_winning: List[str], numbers_have: List[str]):
    num_common = calulate_num_matches(numbers_winning, numbers_have)
    return 2 ** (num_common - 1) if num_common > 0 else 0


if __name__ == "__main__":
    total_points = 0
    num_matching = []

    with open("input.txt", "r", encoding="UTF-8") as file:
        while line := file.readline():
            numbers = line.rstrip().split(":")[1]
            str_win, str_have = numbers.split("|")
            num_win, num_have = re.findall(r"\d+", str_win), re.findall(
                r"\d+", str_have
            )
            total_points += calculate_points(num_win, num_have)
            num_matching.append(calulate_num_matches(num_win, num_have))

    # Part 2
    card_counts = [1] * (len(num_matching))

    for i in range(len(card_counts)):
        cur_count = card_counts[i]

        for j in range(i + 1, min(i + num_matching[i] + 1, len(card_counts))):
            card_counts[j] += cur_count

    print(f"Total number of points = {total_points}")
    print(f"Total number of cards = {sum(card_counts)}")
