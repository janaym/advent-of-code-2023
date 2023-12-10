import re

test_str = 'bfjtdslkdbthree4jvvonezqdthreesrghnnb6six'

def get_calbration_value(str):
  calibration_value = ''

  pattern = r'(\d)'
  first_digit = re.search(pattern, str)

  if not first_digit:
    return 0
  
  else:
    calibration_value += first_digit.group(1)

    # now search from back
    last_digit = re.search(pattern, str[::-1])
    calibration_value += last_digit.group(1)
  
  return calibration_value

print(get_calbration_value(test_str))

with open("/Users/janayma/Documents/advent-of-code-2023/day_01/input.txt", 'r') as f:
  values_sum = 0

  for line in f:
    calibration_value = get_calbration_value(line)
    values_sum += int(calibration_value)

  print('the sum of calibration values is', values_sum)
