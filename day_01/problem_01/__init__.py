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

