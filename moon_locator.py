from datetime import datetime, timedelta
from math import ceil


class MoonLocator:
    moon_on_south = datetime(year=2022, month=11, day=15, hour=6, minute=1, second=12)
    moon_interval = timedelta(days=1, hours=0, minutes=50, seconds=28)

    def next_moon_on_south_from_date(self, from_date: datetime) -> datetime:
        since_moon_on_south = from_date - self.moon_on_south
        cycle = ceil(since_moon_on_south / self.moon_interval)
        return self.moon_on_south + self.moon_interval * cycle

    def other_untested_function() -> int:
        0  # I forgot to add "return" on purpose
