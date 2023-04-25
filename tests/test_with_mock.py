from datetime import datetime, timedelta
from unittest import mock

import pytest

from moon_locator_with_dependency import MoonLocator


@pytest.fixture(scope="module")
def moon_locator():
    return MoonLocator()


namespace = "moon_locator_with_dependency"


@mock.patch(f"{namespace}.reference_date_for_year", return_value=datetime(2020, 2, 1))
def test_date_on_south_a_second_before_should_return_that_date(
    mock_reference, moon_locator
):
    some_moon = datetime(year=2020, month=2, day=1)
    a_moment_before = some_moon - timedelta(seconds=1)

    next_moon = moon_locator.next_moon_on_south_from_date(a_moment_before)

    assert next_moon == some_moon
    mock_reference.assert_any_call(2020)
