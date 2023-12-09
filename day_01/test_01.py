import unittest
from problem_01 import get_calibration_value, convert_spelled_digits

class TestGetCalibrationValues(unittest.TestCase):

  def test_random_string(self):
    '''
    check it works without edge case
    '''
    data = 'pqr3stu8vwx'
    result = get_calibration_value(data, reversed(data))
    self.assertEqual(result, 38)

  def test_list_digit(self):
    '''
    test it can handle a list of integers
    '''
    data = '123456'
    result = get_calibration_value(data, reversed(data))
    self.assertEqual(result, 16)

  def test_no_digits(self):
    '''
    test when no digits, returns zero
    '''
    data = 'abcdef'
    self.assertEqual(get_calibration_value('abcdef', reversed(data)), 0)

  def test_one_digit(self):
    '''
    test when only one digit N present, returns NN
    '''
    data = 'tre7uchet'
    self.assertEqual(get_calibration_value(data, reversed(data)), 77)

  def test_empty_string(self):
    '''
    test it can handle an empty string
    '''
    self.assertEqual(get_calibration_value('', ''), 0)
    
class TestConvertSpelledDigits(unittest.TestCase):
  def test_non_problematic(self):
    self.assertEqual(convert_spelled_digits('abcdef123'), ('abcdef123', '321fedcba'))
  
  def test_spelled_digits(self):
    self.assertEqual(convert_spelled_digits('one'), ('1', '1'))

  def test_overlapping_digits(self):
    self.assertEqual(convert_spelled_digits('twone'), ('2ne', 'tw1'))

if __name__ == '__main__':
  unittest.main()