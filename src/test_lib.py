import unittest

import lib


FLOAT_TOLERANCE = 1e-9


class RectangleTests(unittest.TestCase):
    def test_area_with_different_sides(self):
        actual = lib.rectangle_area(3, 5)
        self.assertEqual(actual, 15)

    def test_area_with_fractional_sides(self):
        actual = lib.rectangle_area(2.5, 1.5)
        self.assertEqual(actual, 3.75)

    def test_area_with_zero_height(self):
        actual = lib.rectangle_area(10, 0)
        self.assertEqual(actual, 0)

    def test_perimeter_with_different_sides(self):
        actual = lib.rectangle_perimeter(3, 5)
        self.assertEqual(actual, 16)

    def test_perimeter_with_fractional_sides(self):
        actual = lib.rectangle_perimeter(2.5, 1.25)
        self.assertEqual(actual, 7.5)

    def test_perimeter_with_equal_sides(self):
        actual = lib.rectangle_perimeter(4, 4)
        self.assertEqual(actual, 16)


class SquareTests(unittest.TestCase):
    def test_area_with_integer_side(self):
        actual = lib.square_area(5)
        self.assertEqual(actual, 25)

    def test_area_with_fractional_side(self):
        actual = lib.square_area(0.5)
        self.assertEqual(actual, 0.25)

    def test_area_with_zero_side(self):
        actual = lib.square_area(0)
        self.assertEqual(actual, 0)

    def test_perimeter_with_integer_side(self):
        actual = lib.square_perimeter(5)
        self.assertEqual(actual, 20)

    def test_perimeter_with_fractional_side(self):
        actual = lib.square_perimeter(0.5)
        self.assertEqual(actual, 2)

    def test_perimeter_with_zero_side(self):
        actual = lib.square_perimeter(0)
        self.assertEqual(actual, 0)


class CircleTests(unittest.TestCase):
    def test_area_with_integer_radius(self):
        actual = lib.circle_area(3)
        self.assertAlmostEqual(actual, 28.274333882308, delta=FLOAT_TOLERANCE)

    def test_area_with_fractional_radius(self):
        actual = lib.circle_area(0.5)
        self.assertAlmostEqual(actual, 0.785398163397, delta=FLOAT_TOLERANCE)

    def test_area_with_zero_radius(self):
        actual = lib.circle_area(0)
        self.assertEqual(actual, 0)

    def test_perimeter_with_integer_radius(self):
        actual = lib.circle_perimeter(3)
        self.assertAlmostEqual(actual, 18.849555921539, delta=FLOAT_TOLERANCE)

    def test_perimeter_with_fractional_radius(self):
        actual = lib.circle_perimeter(0.5)
        self.assertAlmostEqual(actual, 3.141592653590, delta=FLOAT_TOLERANCE)

    def test_perimeter_with_zero_radius(self):
        actual = lib.circle_perimeter(0)
        self.assertEqual(actual, 0)


class TriangleTests(unittest.TestCase):
    def test_area_with_integer_dimensions(self):
        actual = lib.triangle_area(7, 3)
        self.assertEqual(actual, 10.5)

    def test_area_with_fractional_dimensions(self):
        actual = lib.triangle_area(2.5, 1.5)
        self.assertEqual(actual, 1.875)

    def test_area_with_zero_height(self):
        actual = lib.triangle_area(8, 0)
        self.assertEqual(actual, 0)

    def test_perimeter_of_scalene_triangle(self):
        actual = lib.triangle_perimeter(3, 4, 5)
        self.assertEqual(actual, 12)

    def test_perimeter_of_equilateral_triangle(self):
        actual = lib.triangle_perimeter(4, 4, 4)
        self.assertEqual(actual, 12)

    def test_perimeter_with_fractional_sides(self):
        actual = lib.triangle_perimeter(1.5, 2.25, 2.5)
        self.assertEqual(actual, 6.25)
