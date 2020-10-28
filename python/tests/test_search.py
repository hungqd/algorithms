import unittest
from algo.search import binary_search


class SearchAlgorithmsTest(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search(
            [1, 2, 6, 8, 9, 20, 21, 29, 31, 35, 40, 60, 62, 67, 80], 67), 13, "Index should be 13")

        self.assertEqual(binary_search([], 29), None, "Index should be None")

        self.assertEqual(binary_search([10], 10), 0, "Index should be 0")

        self.assertEqual(binary_search([10], 11), None, "Index should be None")

        self.assertEqual(binary_search(
            [-10, -1, 0], -10), 0, "Index should be 0")

        self.assertEqual(binary_search(
            [-10, -1, 0], -1), 1, "Index should be 1")

        self.assertEqual(binary_search(
            [-10, -1, 0], 0), 2, "Index should be 2")

        self.assertEqual(binary_search(
            [-10, -1, 0], -20), None, "Index should be None")

        self.assertEqual(binary_search(
            [-10, -1, 0], -5), None, "Index should be None")

        self.assertEqual(binary_search(
            [-10, -1, 0], 1), None, "Index should be None")

        self.assertEqual(binary_search(
            [-10, -1, 0], 5), None, "Index should be None")


if __name__ == '__main__':
    unittest.main()
