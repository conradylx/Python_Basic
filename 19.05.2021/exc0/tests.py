import unittest

from exc0 import triangle, trapezoid


class FieldsTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 2
        self.b = 3
        self.h = 5

    def test_triangle_with_correct_result(self):
        result = triangle(self.a, self.h)
        self.assertEqual(result, 5)

    def test_triangle_with_incorrect_values(self):
        with self.assertRaises(TypeError):
            triangle("*", self.h)

    def test_trapezoid_with_correct_result(self):
        result = trapezoid(self.a, self.b, self.h)
        self.assertEqual(result, 12.5)

    def test_trapezoid_with_incorrect_value(self):
        with self.assertRaises(TypeError):
            trapezoid('**', self.b, self.h)

    def tearDown(self):
        del self.a, self.h


if __name__ == '__main__':
    unittest.main()
