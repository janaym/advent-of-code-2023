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


# takes in string, converts any spelled digit to a numerical digit
def convert_spelled_digits(str):
    
  spelled_digits = [('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9')]

  new_str = str

  for spelling_pair in spelled_digits:
    spelling = spelling_pair[0]
    i = new_str.find(spelling)
    j = -1
    #if spelling found:
    if i != -1: 
      j = i + len(spelling) 
      new_str = new_str[:i] + spelling_pair[1] + new_str[j:]
      
    
  return new_str



