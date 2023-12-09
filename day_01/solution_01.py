from problem_01 import get_calibration_value, convert_spelled_digits


with open("/Users/janayma/Documents/advent-of-code-2023/day_01/input.txt", 'r') as f:
  sum_values = 0

  for line in f:
    converted_data = convert_spelled_digits(line)
    sum_values += get_calibration_value(converted_data[0], converted_data[1])

  f.close()

print("The total sum of the calibration values is:", sum_values)


# convert_spelled_digits('one')


