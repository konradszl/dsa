import pytest

from .solution import get_concatenation


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
        ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
        ([7], [7, 7]),
        ([5, 5], [5, 5, 5, 5]),
        ([1, 2, 3], [1, 2, 3, 1, 2, 3]),
    ],
)
def test_get_concatenation(nums: list[int], expected: list[int]) -> None:
    assert get_concatenation(nums) == expected
