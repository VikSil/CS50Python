from datetime import date
from seasons import date_diff
import pytest


def test_date_diff():
    dt = date(2023,8,8)
    assert date_diff(dt) == 1440


