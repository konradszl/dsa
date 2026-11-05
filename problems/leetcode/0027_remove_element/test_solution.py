import pytest

from .solution import remove_element


@pytest.mark.parametrize(
    "nums, val, expected",
    [
        ([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
        ([], 1, []),
        ([1, 1, 1], 1, []),
        ([4, 5, 6], 1, [4, 5, 6]),
    ],
)
def test_remove_element(nums: list[int], val: int, expected: list[int]) -> None:
    k = remove_element(nums, val)

    assert k == len(expected)
    assert sorted(nums[:k]) == sorted(expected)
