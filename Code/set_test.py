from sets import Treeset
import unittest

class TreesetTest(unittest.TestCase):
    def test_init(self):
        set = Treeset()
        assert set.size == 0

    def test_contains_with_numbers(self):
        set = Treeset([2, 1, 3])
        assert set.contains(2) is True
        assert set.contains(1) is True
        assert set.contains(3) is True

        assert set.contains(4) is False
        assert set.contains(0) is False

    def test_contains_with_letters(self):
        set = Treeset(['A', 'B', 'C'])
        assert set.contains('A') is True
        assert set.contains('B') is True
        assert set.contains('C') is True

        assert set.contains('D') is False
        assert set.contains('Z') is False


    def test_init_with_list(self):
        set = Treeset([2, 1, 3])
        assert set.contains(2) is True
        assert set.contains(1) is True
        assert set.contains(3) is True
        assert set.size == 3

    def test_init_with_list_of_strings(self):
        set = Treeset(['B', 'A', 'C'])
        assert set.contains('B') is True
        assert set.contains('A') is True
        assert set.contains('C') is True
        assert set.size == 3

    def test_init_with_list_of_tuples(self):
        set = Treeset([(2, 'B'), (1, 'A'), (3, 'C')])
        assert set.contains((2, 'B')) is True
        assert set.contains((1, 'A')) is True
        assert set.contains((3, 'C')) is True
        assert set.size == 3

    def test_size(self):
        set = Treeset()
        assert set.size == 0
        set.add('B')
        assert set.size == 1
        set.add('A')
        assert set.size == 2
        set.add('C')
        assert set.size == 3
        set.remove('A')
        assert set.size == 2
        set.remove('B')
        assert set.size == 1
        set.remove('C')
        assert set.size == 0


    def test_union(self):
        set_1 = Treeset([1, 2, 3])
        set_2 = Treeset([4, 5, 6])
        new_set = set_1.union(set_2)
        assert new_set.contains(1) is True
        assert new_set.contains(2) is True
        assert new_set.contains(3) is True
        assert new_set.contains(4) is True
        assert new_set.contains(5) is True
        assert new_set.contains(6) is True

        assert new_set.contains(7) is False
        assert new_set.contains(0) is False

    def test_intersection(self):
        set_1 = Treeset([1, 2, 3])
        set_2 = Treeset([3, 4, 5])
        new_set = set_1.intersection(set_2)
        assert new_set.contains(3) is True

        assert new_set.contains(1) is False
        assert new_set.contains(2) is False
        assert new_set.contains(4) is False
        assert new_set.contains(5) is False

        set_3 = Treeset([0, 4, 5])
        new_set = set_1.intersection(set_3)
        assert new_set.size == 0

    def test_difference(self):
        set_1 = Treeset([1, 2, 3])
        set_2 = Treeset([3, 4, 5])
        new_set = set_1.difference(set_2)
        assert new_set.contains(3) is False

        assert new_set.contains(1) is True
        assert new_set.contains(2) is True
        assert new_set.contains(4) is False
        assert new_set.contains(5) is False

    def test_is_subset(self):
        set_1 = Treeset([1, 2, 3])
        set_2 = Treeset([1, 2, 3, 4, 5])

        assert set_1.is_subset(set_2) is True
        assert set_2.is_subset(set_1) is False

if __name__ == '__main__':
    unittest.main()