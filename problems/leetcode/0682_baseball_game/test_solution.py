import pytest

from .solution import cal_points


@pytest.mark.parametrize(
    "operations, expected",
    [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1", "C"], 0),
        (["7"], 7),
        (["-3", "D"], -9),
        (["10", "20", "+", "+"], 110),
        (["1", "2", "C", "3", "+"], 8),
    ],
)
def test_cal_points(operations: list[str], expected: int) -> None:
    assert cal_points(operations) == expected
