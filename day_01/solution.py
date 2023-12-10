import re

# soln for part 1
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

# soln for part 2
def get_calbration_value_2(str):
  calibration_value = ''

  digit_spellings_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
  }
  
  # search forwards
  pattern = r'(\d|' + '|'.join(digit_spellings_dict.keys()) + ')'
  first_digit = re.search(pattern, str).group(1)
  if first_digit.isnumeric():
    calibration_value += first_digit
  else:
    first_digit = digit_spellings_dict[first_digit]
    calibration_value += first_digit

  # setup reverse string searching dictionary and pattern
  reversed_spellings_dict = {key[::-1]: value for key, value in digit_spellings_dict.items()}
  reverse_pattern = pattern = r'(\d|' + '|'.join(reversed_spellings_dict.keys()) + ')'

  
  # search in reverse
  last_digit = re.search(reverse_pattern, str[::-1]).group(1)
  if last_digit.isnumeric():
    calibration_value += last_digit
  else:
    calibration_value += reversed_spellings_dict[last_digit]

  return calibration_value




with open("/Users/janayma/Documents/advent-of-code-2023/day_01/input.txt", 'r') as f:
  # using solution no.2
  values_sum = 0

  for line in f:
    calibration_value = get_calbration_value_2(line)
    values_sum += int(calibration_value)

  print('the sum of calibration values is', values_sum)
  f.close()
