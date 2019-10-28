import unittest
import evolutionary_regression


if __name__ == '__main__':
    unittest.main()

class MyTestCase(unittest.TestCase):
    def test_sum_deviation_squared(self):
        p = [(1, 1), (2, 3), (3, 3)]
        test_line = evolutionary_regression.Line(1, 0)
        result = evolutionary_regression.sum_deviation_squared(p, test_line)
        self.assertEqual(result, 1)

        p = [(1, 4), (2, 4), (3, 4)]
        test_line = evolutionary_regression.Line(1, 0)
        result = evolutionary_regression.sum_deviation_squared(p, test_line)
        self.assertEqual(result, 14)

        p = [(1, 0), (2, 0), (3, 0)]
        test_line = evolutionary_regression.Line(1, 0)
        result = evolutionary_regression.sum_deviation_squared(p, test_line)
        self.assertEqual(result, 14)

    def test_new_child_values_change(self):
        test_line = evolutionary_regression.Line(1, 0)
        test_child_line = evolutionary_regression.new_child(test_line)
        self.assertNotEqual(test_line.slope, test_child_line.slope)
        self.assertNotEqual(test_line.constant, test_child_line.constant)

    def test_new_child_creates_new_line(self):
        test_line = evolutionary_regression.Line(1, 0)
        test_child_line = evolutionary_regression.new_child(test_line)
        self.assertNotEqual(test_line, test_child_line)

    def test_choose_heir_best_child_is_line(self):
        p = [(1, 4), (2, 4), (3, 4)]
        test_child_1 = evolutionary_regression.Line(1, 0)
        test_child_2 = evolutionary_regression.Line(2, 1)
        test_child_3 = evolutionary_regression.Line(.2, 3)
        children = (test_child_1, test_child_2, test_child_3)
        heir = evolutionary_regression.choose_heir(p, children)
        self.assertIsInstance(heir, evolutionary_regression.Line, "Heir is line")

    def test_choose_heir_actually_chooses_best_heir(self):
        p = [(1, 4), (2, 4), (3, 4)]
        test_child_1 = evolutionary_regression.Line(1, 0)
        test_child_2 = evolutionary_regression.Line(2, 1)
        test_child_3 = evolutionary_regression.Line(.2, 3)
        children = (test_child_1, test_child_2, test_child_3)
        heir = evolutionary_regression.choose_heir(p, children)
        self.assertEqual(heir, test_child_3)



