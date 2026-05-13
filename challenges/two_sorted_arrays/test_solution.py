from challenges.two_sorted_arrays.two_sorted_arrays import Solution


class TestCuadratic:
    def test_it_returns_true_if_2_numbers_add_up_to_target(self):
        solution = Solution()
        nums = [1, 3, 4, 6, 8, 10, 13]

        result = solution.cuadratic(nums, 13)

        assert result is True

    def test_it_returns_fals_if_no_target_sum(self):
        solution = Solution()
        nums = [1, 3, 4, 6, 8, 10, 13]

        result = solution.cuadratic(nums, 6)

        assert result is False


class TestOptimal:
    def test_it_returns_true_if_2_numbers_add_up_to_target(self):
        solution = Solution()
        nums = [1, 3, 4, 6, 8, 10, 13]

        result = solution.find_2_sum(nums, 13)

        assert result is True

    def test_it_returns_fals_if_no_target_sum(self):
        solution = Solution()
        nums = [1, 3, 4, 6, 8, 10, 13]

        result = solution.find_2_sum(nums, 6)

        assert result is False
