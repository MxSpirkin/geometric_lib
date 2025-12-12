
def area(a):
    return a * a


def perimeter(a):
    return 4 * a

import unittest

# Класс для тестирования функций квадрата
class SquareTestCase(unittest.TestCase):
    # ========== Тесты для функции area(a) ==========
    def test_area_normal(self):
        """Площадь квадрата со стороной 5 должна быть 25."""
        self.assertEqual(area(5), 25)  # 5 * 5 = 25

    def test_area_zero(self):
        """Площадь квадрата со стороной 0 должна быть 0."""
        self.assertEqual(area(0), 0)

    def test_area_fractional(self):
        """Площадь квадрата со стороной 2.5 должна быть 6.25."""
        self.assertEqual(area(2.5), 6.25)  # 2.5 * 2.5 = 6.25

    def test_area_one(self):
        """Площадь квадрата со стороной 1 должна быть 1."""
        self.assertEqual(area(1), 1)

    # ========== Тесты для функции perimeter(a) ==========
    def test_perimeter_normal(self):
        """Периметр квадрата со стороной 5 должен быть 20."""
        self.assertEqual(perimeter(5), 20)  # 4 * 5 = 20

    def test_perimeter_zero(self):
        """Периметр квадрата со стороной 0 должен быть 0."""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_fractional(self):
        """Периметр квадрата со стороной 1.5 должен быть 6."""
        self.assertEqual(perimeter(1.5), 6.0)  # 4 * 1.5 = 6.0

    def test_perimeter_one(self):
        """Периметр квадрата со стороной 1 должен быть 4."""
        self.assertEqual(perimeter(1), 4)

# Блок для запуска тестов при непосредственном выполнении файла
if __name__ == "__main__":
    unittest.main()
