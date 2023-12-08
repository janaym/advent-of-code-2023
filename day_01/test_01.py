import unittest
from problem_01 import getCalibrationValues

class TestGetCalibrationValues(unittest.TestCase):
  def test_list_digit(self):
    '''
    test it can handle a list of integers
    '''

    data = '123'
    result = getCalibrationValues(data)
    self.assertEqual(result, 13)

if __name__ == '__main__':
  unittest.main()