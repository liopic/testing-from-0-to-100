from datetime import datetime, timedelta

import pytest

from moon_locator import MoonLocator


@pytest.fixture(scope="module")
def moon_locator():
    return MoonLocator()


@pytest.fixture
def moon_on_south():
    yield datetime(year=2022, month=11, day=15, hour=6, minute=1, second=12)


def test_date_on_south_a_second_before_should_return_that_date(
    moon_locator, moon_on_south
):
    a_moment_before = moon_on_south - timedelta(seconds=1)

    next_moon = moon_locator.next_moon_on_south_from_date(a_moment_before)

    assert next_moon == moon_on_south
