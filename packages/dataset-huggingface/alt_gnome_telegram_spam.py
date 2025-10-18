from spamirai_dataset_common import DataItem, DataLabel
from src import BaseHuggingFaceImporter


class Importer(BaseHuggingFaceImporter):
    """
    https://huggingface.co/datasets/alt-gnome/telegram-spam
    """

    def __init__(self):
        super().__init__(
            "alt-gnome/telegram-spam",
            "300_huggingface_alt_gnome_telegram_spam",
        )

    def filter_item(self, item: dict) -> bool:
        return True

    def map_item(self, item: dict) -> DataItem:
        return DataItem(
            item["text"],
            DataLabel.SPAM if item["label"] == 1 else DataLabel.NOT_SPAM,
            self.source,
        )


def main():
    Importer().run()


if __name__ == "__main__":
    main()
