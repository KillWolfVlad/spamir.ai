import csv
from pathlib import Path

import pandas as pd

from .data_item import DataItem


class Dataset:
    def __init__(self, dataset_path: Path):
        self._dataset_path = dataset_path
        self._text_cache = set()

        if self._dataset_path.exists():
            df = pd.read_csv(self._dataset_path)
            self._text_cache = set(df["text"])

    def add(self, data_item: DataItem) -> bool:
        if data_item.text in self._text_cache:
            return False

        if not data_item.text:
            return False

        self._text_cache.add(data_item.text)

        dataset_exists = self._dataset_path.exists()

        with open(self._dataset_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if not dataset_exists:
                writer.writerow(["text", "label", "source", "id"])

            writer.writerow(
                [
                    data_item.text,
                    data_item.label.value,
                    data_item.source,
                    str(data_item.id),
                ]
            )

        return True
