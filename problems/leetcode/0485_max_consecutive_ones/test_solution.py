import pytest

from .solution import find_max_consecutive_ones


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
        ([1, 1, 1, 1], 4),
        ([1], 1),
        ([0, 0, 0], 0),
        ([], 0),
    ],
)
def test_find_max_consecutive_ones(nums: list[int], expected: int) -> None:
    assert find_max_consecutive_ones(nums) == expected
