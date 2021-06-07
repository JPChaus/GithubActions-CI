# Jackson E. Rollins 6/6/2021 - Tests for Github Actions

import unittest
import calc


class Testcase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.addition(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(4, 3), 12)

    def test_division(self):
        self.assertEqual(calc.division(60, 2), 30)


if __name__ == '__main__':
    unittest.main()
