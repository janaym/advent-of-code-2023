def getCalibrationValue(str):
  calibrationValue = '0'

  #loop forwads until finds digit
  for char in str:
    if char.isnumeric():
      calibrationValue += char
      break

  #loops backwards until finds digit
  for char in reversed(str):
    if char.isnumeric():
      calibrationValue += char
      break

  return int(calibrationValue)

#checks a string for spelled digits and returns an array containing 
def check_for_spelled_digits(str):

  string_fragments = [];

  spelled_digits = [{'one': 1}, {'two': 2}, {'three': 3}, {'four': 4}, {'five': 5}, {'six': 6}, {'seven': 7}, {'eight': 8}, {'nine': 9}]

  for spelling in spelled_digits:
    spelling_start_index = str.find(spelling)
    spelling_end_index = i + str.len() + 1
    string_fragments.append((str[0:spelling_start_index], str[spelling_end_index:-1]))
  
  return string_fragments




