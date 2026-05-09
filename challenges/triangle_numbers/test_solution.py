from triangle_numbers.triangle_numbers import Solution


def test_it_solves_example_1():

    nums = [11, 4, 9, 6, 15, 18]

    assert Solution.solve(nums) == 10


def test_it_solves_example_2():

    nums = [4, 10, 21, 14]

    assert Solution.solve(nums) == 1


def test_it_solves_example_3():

    nums = [4, 10, 21, 14, 1, 3, 6]

    assert Solution.solve(nums) == 3


def test_it_solves_example_4():

    nums = [3, 5, 7, 6]

    assert Solution.solve(nums) == 4
