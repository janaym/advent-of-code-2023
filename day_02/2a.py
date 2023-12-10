import re

cube_count = {'red': 12, 'green': 13, 'blue': 14} #red, green, blue



str = 'Game 100: 9 blue, 4 red; 5 green, 10 blue, 11 red; 1 green, 1 red; 1 green, 5 red, 1 blue'
print(re.search(r'(\d+)', str).group(1)) 


def is_game_possible(str, cube_count):
  pattern = r'(\d+)\s(\w+)'

  match = re.search(pattern, str)
  while match:

    color = match.group(2)
    count = match.group(1)

    if cube_count[color] < int(count):
      print('found color count too high:', color, count)
      return False

    str = re.split(r'\d+\s\w+', str, maxsplit=1)[1]
    match = re.search(pattern, str)

  return True
  

print(is_game_possible(str, cube_count))


with open("/Users/janayma/Documents/advent-of-code-2023/day_02/input.txt", 'r') as f:
  id_sum = 0
  for line in f:
    #get id:
    game_id = int(re.search(r'(\d+)', line).group(1))
    if (is_game_possible(line, cube_count)):
      id_sum += game_id

  print('the sum of ids is:', id_sum)

  f.close()




