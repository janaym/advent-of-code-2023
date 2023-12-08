import unittest
from problem_01 import getCalibrationValues

class TestGetCalibrationValues(unittest.TestCase):

  def test_random_string(self):
    '''
    check it works without edge case
    '''
    self.assertEqual(getCalibrationValues('pqr3stu8vwx'), 38)

  def test_list_digit(self):
    '''
    test it can handle a list of integers
    '''

    data = '123'
    result = getCalibrationValues(data)
    self.assertEqual(result, 13)

  def test_no_digits(self):
    '''
    test when no digits, returns zero
    '''
    self.assertEqual(getCalibrationValues('abcdef'), 0)

  def test_one_digit(self):
    '''
    test when only one digit N present, returns NN
    '''
    self.assertEqual(getCalibrationValues('treb7uchet'), 77)


if __name__ == '__main__':
  unittest.main()