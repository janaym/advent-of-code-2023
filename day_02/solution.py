import re

cube_count = {'red': 12, 'green': 13, 'blue': 14} #red, green, blue

def is_game_possible(str, cube_count):
  pattern = r'(\d+)\s(\w+)'

  match = re.search(pattern, str)
  while match:

    color = match.group(2)
    count = match.group(1)

    if cube_count[color] < int(count):
      return False

    str = re.split(r'\d+\s\w+', str, maxsplit=1)[1]
    match = re.search(pattern, str)

  return True

def get_min_cube_set(str):
  pattern = r'(\d+)\s(\w+)'
  highest_color_counts = {'red': 0, 'blue': 0, 'green': 0}

  match = re.search(pattern, str)
  while match:
    
    color = match.group(2)
    count = int(match.group(1))

    if highest_color_counts[color] < count:
      highest_color_counts[color] = count
    
    str = re.split(r'\d+\s\w+', str, maxsplit=1)[1]
    match = re.search(pattern, str)
  
  return highest_color_counts

print(get_min_cube_set(str))

with open("/Users/janayma/Documents/advent-of-code-2023/day_02/input.txt", 'r') as f:

  #2a
  id_sum = 0
  power_sum = 0
  for line in f:
    #part 1
    game_id = int(re.search(r'(\d+)', line).group(1))
    if (is_game_possible(line, cube_count)):
      id_sum += game_id

    #part 2
    power = 1
    min_set = get_min_cube_set(line)
    for color in min_set:
      power *= min_set[color]

    power_sum += power

  print('the sum of ids is:', id_sum)
  print('the sume of all game powers is: ', power_sum)

    
  f.close()




