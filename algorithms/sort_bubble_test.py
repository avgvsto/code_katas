import pytest

from algorithms.sort_bubble import sort_bubble


@pytest.mark.parametrize(
    "iterable,expected",
    [
        ([1, 4, 5, 2, 6], [1, 2, 4, 5, 6]),
        ([22, 0, 99, 21, 23, 6], [0, 6, 21, 22, 23, 99]),
        ([-2, 19, 0, -1], [-2, -1, 0, 19]),
        ([0.5, 2, 0.9, -1.2], [-1.2, 0.5, 0.9, 2]),
        (["a", "x", "b"], ["a", "b", "x"]),
        (("a", "x", "b"), ["a", "b", "x"]),
        ({"a", "x", "b"}, ["a", "b", "x"]),
    ],
)
def test_it_sorts_a_list(iterable, expected):

    sorted = sort_bubble(iterable)

    assert sorted == expected
