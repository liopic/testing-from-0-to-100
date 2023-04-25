from datetime import datetime, timedelta

from moon_locator import MoonLocator


def test_date_on_south_a_second_before_should_return_that_date():
    sut = MoonLocator()
    some_moon_on_south = datetime(
        year=2022, month=11, day=15, hour=6, minute=1, second=12
    )
    a_moment_before = some_moon_on_south - timedelta(seconds=1)

    next_moon = sut.next_moon_on_south_from_date(a_moment_before)

    assert next_moon == some_moon_on_south, ""


def test_next_moon_on_south_should_be_in_the_future():
    sut = MoonLocator()
    some_date = datetime(2022, 12, 14, 0, 0, 0)  # This could be random!

    next_moon = sut.next_moon_on_south_from_date(some_date)

    assert next_moon >= some_date


def test_next_moon_should_be_between_a_date_and_one_day_one_hour_later():
    sut = MoonLocator()
    some_date = datetime(2022, 12, 14, 0, 0, 0)  # This could be random!
    one_day_one_hour_later = some_date + timedelta(days=1, hours=1)

    next_moon = sut.next_moon_on_south_from_date(some_date)

    assert next_moon >= some_date
    assert one_day_one_hour_later >= next_moon


def test_next_moon_on_south():
    sut = MoonLocator()
    some_date = datetime(2022, 12, 14, 0, 0, 0)

    next_moon = sut.next_moon_on_south_from_date(some_date)

    assert next_moon == datetime(
        2022, 12, 14, 5, 34, 16
    ), "Something has failed but I can not say what or where"
