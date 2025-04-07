# tests/test_base.py
import unittest

class TestBase(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(1 + 1, 2)

