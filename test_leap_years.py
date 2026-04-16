import unittest

class SmokeTest(unittest.TestCase):
    def test1_and_1(self):
        self.assertEqual(1+1, 2)
        
if __name__ == "__main__":
    unittest.main()