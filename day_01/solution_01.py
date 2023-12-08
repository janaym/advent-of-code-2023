from problem_01 import getCalibrationValue

with open("/Users/janayma/Documents/advent-of-code-2023/day_01/input_01.txt", 'r') as f:
  sum_values = 0

  for line in f:
    sum_values += getCalibrationValue(line)

  f.close()

print("The total sum of the calibration values is:", sum_values)