from abc import ABC, abstractmethod
from typing import Generator, Iterable

from .data_item import DataItem
from .data_label import DataLabel
from .dataset import Dataset
from .dataset_paths import dataset_paths


class BaseImporter(ABC):
    def __init__(self, layer_name: str):
        self._dataset = Dataset(
            dataset_paths.get_dataset_layer_path(layer_name),
        )

    @abstractmethod
    def load_dataset(self) -> Generator[dict, None, None]:
        pass

    @abstractmethod
    def filter_item(self, item: dict) -> bool:
        pass

    @abstractmethod
    def map_item(self, item: dict) -> DataItem | Iterable[DataItem]:
        pass

    def run(self):
        count = 0
        imported = 0
        filtered = 0
        spam_count = 0
        not_spam_count = 0

        def print_stats():
            print(
                f"imported {imported}/{count} messages | filtered {filtered} | spam {spam_count} | not spam {not_spam_count}",
            )

        for item in self.load_dataset():
            count += 1

            if not self.filter_item(item):
                filtered += 1
                print_stats()

                continue

            data_items = self.map_item(item)

            if isinstance(data_items, DataItem):
                data_items = [data_items]

            for data_item in data_items:
                if self._dataset.add(data_item):
                    imported += 1

                    match data_item.label:
                        case DataLabel.SPAM:
                            spam_count += 1
                        case DataLabel.NOT_SPAM:
                            not_spam_count += 1

            print_stats()
