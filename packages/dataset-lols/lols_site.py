from datetime import date, timedelta
from typing import Generator, Iterable

from spamirai_dataset_common import BaseImporter, DataItem, DataLabel
from src import dates_cache, fetch_messages


class Importer(BaseImporter):
    def __init__(self, current_date: date):
        super().__init__("200_lols_site")

        self._current_date = current_date

    def load_dataset(self) -> Generator[dict, None, None]:
        for message in fetch_messages(self._current_date):
            yield message

    def filter_item(self, item: dict) -> bool:
        return True

    def map_item(self, item: dict) -> DataItem | Iterable[DataItem]:
        return DataItem(item["text"], DataLabel.SPAM, "lols-site")


def main():
    current_date = date(2015, 1, 1)
    today = date.today()

    while current_date <= today:
        if current_date not in dates_cache:
            print(current_date)
            Importer(current_date).run()

            if current_date != today:
                dates_cache.add(current_date)

        current_date += timedelta(days=1)


if __name__ == "__main__":
    main()
