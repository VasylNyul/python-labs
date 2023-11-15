import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_addition_positive_numbers(self):
        result = calculator.calculate(5, 3, '+', 0)
        self.assertEqual(result, 8)

    def test_addition_negative_numbers(self):
        result = calculator.calculate(-5, -3, '+', 0)
        self.assertEqual(result, -8)

    def test_subtraction(self):
        result = calculator.calculate(5, 3, '-', 0)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = calculator.calculate(5, 3, '*', 0)
        self.assertEqual(result, 15)

    def test_multiplication_with_zero(self):
        result = calculator.calculate(5, 0, '*', 0)
        self.assertEqual(result, 0)

    def test_multiplication_with_negative_numbers(self):
        result = calculator.calculate(-5, 3, '*', 0)
        self.assertEqual(result, -15)

    def test_division(self):
        result = calculator.calculate(6, 2, '/', 0)
        self.assertEqual(result, 3)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.calculate(6, 0, '/', 0)

    def test_errors(self):
        with self.assertRaises(ValueError):
            calculator.calculate(5, 3, '+', -2)
            calculator.calculate('1', '2', '+', 0)
            calculator.calculate(5, 3, '$', 0)


if __name__ == '__main__':
    unittest.main()
