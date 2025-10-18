import os
from typing import Generator

from dotenv import load_dotenv
from spamirai_dataset_common import BaseImporter, DataItem, DataLabel
from spamirai_dataset_telegram_common import ChatHistoryReader


class Importer(BaseImporter):
    def __init__(self):
        super().__init__(os.getenv("DATASET_LAYER_NAME"))

        self._default_label = DataLabel(os.getenv("DEFAULT_LABEL"))
        self._default_source = os.getenv("DEFAULT_SOURCE")

    def load_dataset(self) -> Generator[dict, None, None]:
        chat_history_reader = ChatHistoryReader(
            os.getenv("CHAT_HISTORY_PATH"),
        )

        for message in chat_history_reader.read_all():
            yield {"text": message}

    def filter_item(self, item: dict) -> bool:
        return True

    def map_item(self, item: dict) -> DataItem:
        return DataItem(
            item["text"],
            self._default_label,
            self._default_source,
        )


def main():
    load_dotenv()

    Importer().run()


if __name__ == "__main__":
    main()
