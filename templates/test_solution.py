import pytest

from .solution import func_name


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], 0),
    ],
)
def test_func_name(nums: list[int], expected: int) -> None:
    assert func_name(nums) == expected
