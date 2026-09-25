from datetime import date

import pytest

from app.schemas.base import TransfermarktBaseModel


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("03/12/2025", date(2025, 12, 3)),  # day <= 12: was read as 12 Mar
        ("25/12/2025", date(2025, 12, 25)),
        ("01/07/2021", date(2021, 7, 1)),
        ("12.03.2025", date(2025, 3, 12)),
        ("Dec 3, 2025", date(2025, 12, 3)),
        ("2025-03-12", date(2025, 3, 12)),  # ISO must not be flipped
        ("2025-03-12T10:00:00", date(2025, 3, 12)),
        ("-", None),
        ("", None),
        (None, None),
    ],
)
def test_parse_str_to_date_is_day_first(raw, expected):
    assert TransfermarktBaseModel.parse_str_to_date(raw) == expected
