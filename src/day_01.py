import regex as re

with open('./data/puzzle_input_day_01.txt') as f:
    lines = f.read().split('\n')

regex_digits_only = r'\d'
regex_digits_and_letters = r'one|two|three|four|five|six|seven|eight|nine|\d'

translation_dict = {
    '1': 1,
    '2': 2,
    'one': 1,
    'two': 2,
    '3': 3,
    'three': 3,
    '4': 4,
    'four': 4,
    '5': 5,
    'five': 5,
    '6': 6,
    'six': 6,
    '7': 7,
    'seven': 7,
    '8': 8,
    'eight': 8,
    '9': 9,
    'nine': 9
}

filtered_lines = [
    [ translation_dict[i] for i in re.findall(regex_digits_only, line)] for line in lines
]

result = sum(
    [int(str(i[0]) + str(i[-1])) for i in filtered_lines]
)

print("Part One:", result)

filtered_lines = [
    [ translation_dict[i] for i in re.findall(regex_digits_and_letters, line, overlapped=True)] for line in lines
]

result = sum(
    [int(str(i[0]) + str(i[-1])) for i in filtered_lines]
)

print("Part Two:", result)