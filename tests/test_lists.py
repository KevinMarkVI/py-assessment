import unittest

from assessments import lists


class ListsTestCase(unittest.TestCase):

    def setUp(self):
        self.list = [1, 2, 3, 4, 5]

    def test_largest_item(self):
        """Should return the largest integer element of given list"""
        result = lists.largest_item(self.list)
        self.assertEqual(result, 5)

    def test_count_evens(self):
        """Should return the counter of even integers in given list"""
        result = lists.count_evens(self.list)
        self.assertEqual(result, 2)  # even values: 2, 4
