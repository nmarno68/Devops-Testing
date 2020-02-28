import unittest
from GameDriverTests.StartAnotherGameTests import StartAnotherGameTests


def game_driver_test_suite():

    # Create GameDriver Test Suite
    game_driver_tests = unittest.TestSuite()
    game_driver_tests.addTest(StartAnotherGameTests())

    return game_driver_tests


if __name__ == '__main__':
    suite = game_driver_test_suite()

    runner = unittest.TextTestRunner()
    runner.run(suite)
