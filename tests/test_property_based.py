from datetime import datetime

from hypothesis import given, settings
import hypothesis.strategies as st

from moon_locator import MoonLocator

datetimes = st.datetimes(max_value=datetime(2100, 1, 1))


@given(datetimes)
@settings(max_examples=5000)
def test_next_moon_should_be_after_some_given_date(date):
    moon_locator = MoonLocator()
    next_moon = moon_locator.next_moon_on_south_from_date(date)
    assert next_moon >= date
