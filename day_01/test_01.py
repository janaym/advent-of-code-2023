import unittest
from problem_01 import getCalibrationValue

class TestGetCalibrationValues(unittest.TestCase):

  def test_random_string(self):
    '''
    check it works without edge case
    '''
    data = 'pqr3stu8vwx'
    result = getCalibrationValue(data)
    self.assertEqual(result, 38)

  def test_list_digit(self):
    '''
    test it can handle a list of integers
    '''
    data = '123456'
    result = getCalibrationValue(data)
    self.assertEqual(result, 16)

  def test_no_digits(self):
    '''
    test when no digits, returns zero
    '''
    self.assertEqual(getCalibrationValue('abcdef'), 0)

  def test_one_digit(self):
    '''
    test when only one digit N present, returns NN
    '''
    self.assertEqual(getCalibrationValue('treb7uchet'), 77)

  def test_empty_string(self):
    '''
    test it can handle an empty string
    '''
    self.assertEqual(getCalibrationValue(''), 0)


if __name__ == '__main__':
  unittest.main()