import pytest

from challenges.trapping_rain_water.trapping_rain_water import Solution


@pytest.mark.parametrize(
    "walls,expected",
    [
        ([3, 4, 1, 2, 2, 5, 1, 0, 2], 10),
        ([10, 0, 8, 0, 10], 22),
        ([10, 0, 8, 0, 11], 22),
        ([5, 10, 8, 12, 13, 20, 10, 10, 12], 2 + 4),
    ],
)
def test_on_solution(walls, expected):
    solution = Solution()
    result = solution.trapped_water(walls)

    assert result == expected


@pytest.mark.parametrize(
    "walls,expected",
    [
        ([3, 4, 1, 2, 2, 5, 1, 0, 2], 10),
        ([10, 0, 8, 0, 10], 22),
        ([10, 0, 8, 0, 11], 22),
        ([5, 10, 8, 12, 13, 20, 10, 10, 12], 2 + 4),
    ],
)
def test_brute(walls, expected):
    solution = Solution()

    result = solution.brute_force_solution(walls)

    assert result == expected
