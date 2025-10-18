import csv
from datetime import date

import pandas as pd
from spamirai_dataset_common import cache_paths


class DatesCache:
    def __init__(self):
        self._dates_cache = set()
        self._dates_cache_path = cache_paths.get_cache_dir("lols") / "dates.csv"

        if self._dates_cache_path.exists():
            df = pd.read_csv(self._dates_cache_path, parse_dates=["date"])
            self._dates_cache = set(df["date"].dt.date)

    def __contains__(self, value: date) -> bool:
        return value in self._dates_cache

    def add(self, value: date):
        if value in self:
            return

        self._dates_cache.add(value)

        dates_cache_path = self._dates_cache_path.exists()

        with open(self._dates_cache_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if not dates_cache_path:
                writer.writerow(["date"])

            writer.writerow([value])


dates_cache = DatesCache()
