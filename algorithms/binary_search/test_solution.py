from binary_search.binary_search import BinarySearch


class TestValue:
    def test_example_1(self):

        nums = [1, 3, 5, 7, 9]
        target = 6

        assert BinarySearch.find(nums, target) == 7

    def test_example_2(self):

        nums = [1, 3, 5, 7, 9]
        target = 10

        assert BinarySearch.find(nums, target) == -1

    def test_example_3(self):

        nums = [2, 4, 6, 8]
        target = 2

        assert BinarySearch.find(nums, target) == 2

    def test_example_4(self):

        nums = [2, 4, 6, 8, 10, 23, 55, 66, 100, 200]
        target = 6

        assert BinarySearch.find(nums, target) == 6


class TestIndex:
    def test_moves_to_right(self):

        nums = [1, 3, 5, 7, 9]
        target = 6

        assert BinarySearch.find_index(nums, target) == 3

    def test_moves_to_right_without_result(self):

        nums = [1, 3, 5, 7, 9]
        target = 10

        assert BinarySearch.find_index(nums, target) == -1

    def test_example_moves_to_left(self):

        nums = [2, 4, 6, 8]
        target = 2

        assert BinarySearch.find_index(nums, target) == 0

    def test_example_moves_to_left_long(self):

        nums = [2, 4, 6, 8, 10, 23, 55, 66, 100, 200]
        target = 6

        assert BinarySearch.find_index(nums, target) == 2

    def test_example_moves_to_left_duplicate(self):

        nums = [2, 4, 6, 6, 8, 10, 23, 55, 66, 100, 200]
        target = 6

        assert BinarySearch.find_index(nums, target) == 2
