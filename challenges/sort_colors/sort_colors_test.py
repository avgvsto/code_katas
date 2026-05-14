import pytest

from challenges.sort_colors.sort_colors import sort_numbers_as_colors


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 1, 2, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 1, 1, 1, 2, 2]),
        ([2, 2, 2, 2, 2, 2, 0, 0, 0, 1], [0, 0, 0, 1, 2, 2, 2, 2, 2, 2]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
        ([0, 0, 0], [0, 0, 0]),
    ],
)
def test_it_sorts_numbers_as_colors(nums, expected):

    sort_numbers_as_colors(nums)

    assert nums == expected


@pytest.mark.parametrize(
    "nums",
    [
        ([-1, 0, 1, 2]),
        (["1", 0, 1, 2]),
    ],
)
def test_it_raises_on_invalid_color(nums):

    with pytest.raises(TypeError):
        sort_numbers_as_colors(nums)
