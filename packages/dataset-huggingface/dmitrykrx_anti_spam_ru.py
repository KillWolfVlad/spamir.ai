from spamirai_dataset_common import DataItem, DataLabel
from src import BaseHuggingFaceImporter


class Importer(BaseHuggingFaceImporter):
    """
    https://huggingface.co/datasets/DmitryKRX/anti_spam_ru
    """

    def __init__(self):
        super().__init__(
            "DmitryKRX/anti_spam_ru",
            "310_huggingface_dmitrykrx_anti_spam_ru",
        )

    def filter_item(self, item: dict) -> bool:
        return True

    def map_item(self, item: dict) -> DataItem:
        return DataItem(
            item["text"],
            DataLabel.SPAM if item["is_spam"] == 1 else DataLabel.NOT_SPAM,
            self.source,
        )


def main():
    Importer().run()


if __name__ == "__main__":
    main()
