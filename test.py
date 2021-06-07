# Jackson E. Rollins 6/6/2021 - Tests for Github Actions

import unittest
import calc


class Testcase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.addition(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
