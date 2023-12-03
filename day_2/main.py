from typing import List


def is_valid(rgb_max: List[int]) -> bool:
    return rgb_max[0] <= 12 and rgb_max[1] <= 13 and rgb_max[2] <= 14


def get_power(rgb_max: List[int]) -> int:
    return rgb_max[0] * rgb_max[1] * rgb_max[2]


def get_game_data(raw_string: str) -> List[int]:
    rgb_max = [0, 0, 0]
    hands = raw_string.split(";")

    for hand in hands:
        entities = hand.split(" ")

        for i in range(len(entities)):
            entity = entities[i]

            if entity.startswith("red"):
                rgb_max[0] = max(rgb_max[0], int(entities[i - 1]))

            if entity.startswith("green"):
                rgb_max[1] = max(rgb_max[1], int(entities[i - 1]))

            if entity.startswith("blue"):
                rgb_max[2] = max(rgb_max[2], int(entities[i - 1]))

    return rgb_max


if __name__ == "__main__":
    games_data = []
    valid_id_sum, rgb_power_sum = 0, 0

    with open("input.txt", "r", encoding="UTF-8") as file:
        while line := file.readline():
            game_data = get_game_data(line.rstrip().split(":")[1])
            games_data.append(game_data)

    for i in range(len(games_data)):
        valid_id_sum += (i + 1) if is_valid(games_data[i]) else 0

    for i in range(len(games_data)):
        rgb_power_sum += get_power(games_data[i])

    print(f"Sum of IDs of valid games = {valid_id_sum}")
    print(f"Sum of powers of min rgb sets = {rgb_power_sum}")