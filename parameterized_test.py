import unittest
from triangle import is_triangle

class TriangleTest(unittest.TestCase):
    valid_triangles = [
        (1, 1, 1),
        (3, 4, 5),
        (3, 4, 6),
        (8, 10, 12),
        (100, 101, 200),
        (0.9, 1.0, 1.1) ]

    not_triangle = [
        (21, 10, 10),
        (2, 1, 1),
        (6, 10, 4),
        (6, 20, 4),
        (2, 2, 5) ]

    invalid_argument = [
        (-1, 2, 2),
        (1, 0, 2),
        (1, -1, 2),
        (2, 3, 6),
        (-2, 3, 6),
        (1, 4, 6),
        (-1, 4, 6),
        (2, 2, 5) ]

    def test_valid_triangle(self):
        for a, b, c in self.valid_triangles:
            with self.subTest():
                msg = f"with the sides ({a}, {b}, {c})"
                self.assertTrue( is_triangle(a, b, c), msg)


    def test_not_triangle(self):
        for a, b, c in self.not_triangle:
            with self.subTest():
                msg = f"with the sides ({a}, {b}, {c})"
                self.assertFalse( is_triangle(a, b, c), msg)


    def test_invalid_argument_raises_exception(self):
        """any non-positive argument should raise ValueError"""
        for a, b, c in self.invalid_argument:
            with self.subTest():
                # msg = f"with the sides ({a}, {b}, {c})"
                with self.assertRaises(ValueError):
                    triangle = is_triangle(a, b, c)