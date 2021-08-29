import unittest
import Assignment.collapse as collapse


class CollapseTest(unittest.TestCase):

# Happy path test
    def test100_100_ShouldCollapseSingleDigit(self):
        value = '5'
        expectedResult = '5'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
    
    
# Happy path test
    def test_ShouldCollapseSingleDigit(self):
        value = '0'
        expectedResult = '0'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
    
    
# Happy path test
    def test_ShouldCollapseAllDigit(self):
        value = '98769'
        expectedResult = '3'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
    
    

# Happy path test
    def test_ShouldCollapseAllDigits(self):
        value = '123'
        expectedResult = '6'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
    
    
# Happy path test
    def test_ShouldNotCollapseLetters(self):
        value = 'abc'
        expectedResult = None 
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
    
    
# Happy path test
    def test_ShouldNotCollapseNoDigit(self):
        value = ''
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
    
    
# Happy path test
    def test_ShouldNotCollapseOverFiftyDigits(self):
        value = '123456789012345678901234567890123456789012345678901'
        expectedResult = None 
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
    
    
