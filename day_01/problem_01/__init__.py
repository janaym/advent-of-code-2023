import re

def get_calibration_value(fwd_str, rvs_str):
  calibrationValue = '0'

  #loop forwads until finds digit
  for char in fwd_str:
    if char.isnumeric():
      calibrationValue += char
      break

  #loops backwards until finds digit
  for char in rvs_str:
    if char.isnumeric():
      calibrationValue += char
      break
  
  return int(calibrationValue)


# # takes in string, converts any spelled digit to a numerical digit
# def convert_spelled_digits(str):
    
#   spelled_digits = [('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9')]

#   fwd_str = str
#   rvs_str = str


#   #convert string backwards and forwards to account for overlapping spellings
#   for spelling_pair in spelled_digits:
#     fwd_str = convert_one_spelling(fwd_str, spelling_pair)

#     rvs_spelling = (spelling_pair[0][::-1], spelling_pair[1])
#     rvs_str = convert_one_spelling(rvs_str[::-1], rvs_spelling)
#   return (fwd_str, rvs_str)


# def convert_one_spelling(str, spelling_pair):
#   spelling = spelling_pair[0]
#   i = str.find(spelling)
#   j = -1
#   new_str = str

#   if i != -1:
#     j = i + len(spelling)
#     new_str = new_str[:i] + spelling_pair[1] + new_str[j:]
#     #recursive step
#     new_str = convert_one_spelling(new_str, spelling_pair)
#   print('returning', new_str)
#   return new_str






