import pytest

from .solution import replace_elements


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]),
        ([400], [-1]),
        ([1, 2], [2, -1]),
        ([5, 4, 3, 2, 1], [4, 3, 2, 1, -1]),
        ([1, 2, 3, 4], [4, 4, 4, -1]),
        ([2, 2, 2], [2, 2, -1]),
    ],
)
def test_replace_elements(arr: list[int], expected: list[int]) -> None:
    assert replace_elements(arr) == expected
