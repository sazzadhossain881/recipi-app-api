"""simple test"""

from django.test import SimpleTestCase
from app import clac


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        """test adding number together"""
        res = clac.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):

        res = clac.subtract(15, 10)

        self.assertEqual(res, 5)
