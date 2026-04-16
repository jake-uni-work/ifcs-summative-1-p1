import unittest

from leap_years import is_leap_year

class SmokeTest(unittest.TestCase):
    def test1_and_1(self):
        self.assertEqual(1+1, 2)
        
        
class LeapYearTests(unittest.TestCase):
    def test_4(self):
        self.assertEqual(is_leap_year(2024), True)
        self.assertEqual(is_leap_year(2026), False)
        
    def test_100(self):
        self.assertEqual(is_leap_year(1800), False)
        
    def test_400(self):
        self.assertEqual(is_leap_year(2000), True)
    
if __name__ == "__main__":
    unittest.main()