from datetime import datetime, timedelta
from math import ceil


def reference_date_for_year(year) -> datetime:
    if year >= 2022:
        return datetime(2022, 11, 15, 6, 1, 12)
    else:
        return datetime(2010, 1, 2, 2, 32, 4)


class MoonLocator:
    moon_interval = timedelta(days=1, hours=0, minutes=50, seconds=28)

    def next_moon_on_south_from_date(self, from_date: datetime) -> datetime:
        moon_on_south = reference_date_for_year(from_date.year)
        since_moon_on_south = from_date - moon_on_south
        cycle = ceil(since_moon_on_south / self.moon_interval)
        return moon_on_south + self.moon_interval * cycle
