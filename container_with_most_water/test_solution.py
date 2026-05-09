from container_with_most_water.container_with_most_water import Solution


def test_it_solves_example_1():

    heights = [3, 4, 1, 2, 2, 4, 1, 3, 2]

    assert Solution.max_area(heights) == 21


def test_it_solves_example_2():

    heights = [1, 2, 1]

    assert Solution.max_area(heights) == 2


def test_it_solves_example_3():

    heights = [3, 5, 2, 100, 100, 1, 3, 9, 4]

    assert Solution.max_area(heights) == 100
