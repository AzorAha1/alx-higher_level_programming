#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
"""Test
testing
"""

class TestRec(unittest.TestCase):
    """Test Rec
    testing my rectangle
    """
    def test_rectangle(self):
            r1 = Rectangle(10, 12)
            r2 = Rectangle(2, 10)
            r3 = Rectangle(10, 2, 0, 0, 12)
            self.assertEqual(r1.id, 1)
            self.assertEqual(r2.id, 2)
            self.assertEqual(r3.id, 12)