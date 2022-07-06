from unittest import TestCase, main
from intersection_of_reactangles.app import find_intersection


class TestFindIntersection(TestCase):

    def test_intersection(self):
        self.assertEqual(find_intersection([-5, 2, 3, -2], [2, 6, 5, 1]), 1.0)
        self.assertEqual(find_intersection([-20, -25, 15, 10], [5, -35, 35, -10]), 150.0)
        self.assertEqual(find_intersection([1.2, 1.2, 3.5, 3.5], [2.1, 2.1, 4.7, 4.7]), 1.9599999999999997)
        self.assertEqual(find_intersection([-3, -10, -5, 5], [10, 22, 13, 44]), False)
        self.assertRaises(BaseException, find_intersection([-3, -10, -5, 5, 5, 5], [10, 22, 13, 44, 5, 5]))
        self.assertRaises(BaseException, find_intersection([-3], [10, 22]))
        self.assertRaises(TypeError, find_intersection(["a", "3", -5, "d"], [10, "a", 13, 44, 5, 5]))


if __name__ == '__main__':
    main()
