import re

with open('./data/puzzle_input_day_02.txt') as f:
    lines = f.read().split('\n')

def parse_game(game):
    game_id, sets = game.split(': ')
    game_id = int(re.findall(r'Game (\d+)', game_id)[0])
    sets = sets.split('; ')

    n_red = max([int(re.findall(r'(\d+) red', s)[0]) for s in sets if 'red' in s])
    n_green = max([int(re.findall(r'(\d+) green', s)[0]) for s in sets if 'green' in s])
    n_blue = max([int(re.findall(r'(\d+) blue', s)[0]) for s in sets if 'blue' in s])
    
    return game_id, n_red, n_green, n_blue

max_red, max_green, max_blue = 12, 13, 14
result_part_one, result_part_two = 0, 0

for game in lines:
    game_id, n_red, n_green, n_blue = parse_game(game)

    if (n_red <= max_red) & (n_green <= max_green) & (n_blue <= max_blue):
        result_part_one += game_id

    result_part_two += n_red * n_green * n_blue

print("Part One:", result_part_one)
print("Part Two:", result_part_two)
