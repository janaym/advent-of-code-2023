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
  print('converting')
    
  spelled_digits = [('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9')]

  new_str = str

  for spelling_pair in spelled_digits:
    print ('before converting 1')
    new_str = convert_one_spelling(new_str, spelling_pair)
    print ('after', new_str)
      
    
  return new_str


def convert_one_spelling(str, spelling_pair):
  print('in one spelling with spelling pair:', spelling_pair)
  spelling = spelling_pair[0]
  i = str.find(spelling)
  j = -1
  print('current string is ', str)
  new_str = str

  if i != -1:
    j = i + len(spelling)
    new_str = new_str[:i] + spelling_pair[1] + new_str[j:]
    print(new_str)
    new_str = convert_one_spelling(new_str, spelling_pair)

  print('returning string from recurision', new_str, i, j)
  return new_str




