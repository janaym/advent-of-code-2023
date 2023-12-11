import re

print(re.search(r'(123)', '123'))
#takes in a start and end index, and returns a box of adjacent indices.
def get_adjacent_indices(start, end, i):

  box_range = range(start-1, end+1)

  top_indices = [(i-1, j) for j in box_range]
  middle_indices = [(i, start - 1), (i, end)]
  bottom_indices = [(i+1, j) for j in box_range]


  # special cases: number is at the boundary
  if i == 0:
    print('at the top!')
    top_indices = []
  elif i == 139:
    print("at the bottom")
    bottom_indices = []

  if end == '\n':
    print("at the end of the line")
    top_indices = top_indices[:-2]
    middle_indices = [(i, start-1)]
    bottom_indices = bottom_indices[:-2]
  elif start == 0:
    print('at the start of the line')
    top_indices = top_indices[1:]
    middle_indices = [(i, end)]
    bottom_indices = bottom_indices[1:]

  return top_indices + middle_indices + bottom_indices
    
#checks all adjacent values in the matrix and returns true if one is a symbol. returns false otherwise
def check_adjacent_values(matrix, indices):
  adjacent_values = ''.join([matrix[coord[0]][coord[1]] for coord in indices])
  symbol = re.search(r'[^.\d]', adjacent_values)

  if symbol:
    #print(symbol)
    return True

  return False

#convert data to matrix
engine_data = []
with open("/Users/janayma/Documents/advent-of-code-2023/day_03/input.txt", 'r') as f:
  for line in f:
    engine_data.append(line)
  

sum_part_numbers = 0

for i,line in enumerate(engine_data):

  #search for number
  numbers = re.findall(r'(\d+)', line)

  for number in numbers:
     #get number start and end indices
    pattern = r'('+ str(number) + ')'
    print(pattern)
    number = re.search(pattern, line)
    number_start = number.span()[0]
    number_end = number.span()[1]
    value = number.group(1)
    print(number, number_start, number_end, value)

    #define box of indices to be checked
    adjacent_indices = get_adjacent_indices(number_start, number_end, i)
    
    has_symbol = check_adjacent_values(engine_data, adjacent_indices)
    
    if has_symbol:
      sum_part_numbers += int(value)


print(sum_part_numbers)












