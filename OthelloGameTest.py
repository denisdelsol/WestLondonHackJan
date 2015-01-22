__author__ = 'root'

import unittest
from OthelloGame import OthelloGame

class MyTestCase(unittest.TestCase):
    def test_something(self):
        game = OthelloGame()
        self.assertIsInstance(game, OthelloGame)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
