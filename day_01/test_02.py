import unittest
from problem_01 import convert_spelled_digits


class TestCheckForSpelledDigits(unittest.TestCase):
  def test_one_spelling(self):
    '''
    test for string with only one digit spelled out
    '''
    self.assertEqual(convert_spelled_digits('one'), '1')

  def test_no_spellings(self):
    '''
    test for string with no spelled digits, returns string unchanged
    '''
    self.assertEqual(convert_spelled_digits('1abcde23fivs4'), '1abcde23fivs4')

  def test_combined_string(self):
    '''
    test with a random string with digits, spelled digits, and other content
    '''
    self.assertEqual(convert_spelled_digits('abcone2threexyz'), 'abc123xyz')

  def test_multiple_instances(self):
    '''
    test handling multiple instances of a spelled digit
    '''
    self.assertEqual(convert_spelled_digits('123fouronefouroneoneabreg2'), '12341411abreg2')

  def test_empty_string(self):
    self.assertEqual(convert_spelled_digits(''), '')

if __name__ == '__main__':
  unittest.main()