import unittest
from GameDriver import GameDriver
import sys
sys.path.append("../BlackJack/")


class StartAnotherGameTests(unittest.TestCase):
    def setup(self):
        self.driver = GameDriver()

    def test_start_another_game_small_y(self):
        self.assertTrue(self.driver.start_another_game('y'))


if __name__ == '__main__':
    unittest.main()
