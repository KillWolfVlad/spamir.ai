from spamirai_dataset_common import DataItem, DataLabel
from src import BaseHuggingFaceImporter


class Importer(BaseHuggingFaceImporter):
    """
    https://huggingface.co/datasets/Deysi/spam-detection-dataset
    """

    def __init__(self):
        super().__init__(
            "Deysi/spam-detection-dataset",
            "320_huggingface_deysi_spam_detection_dataset",
        )

    def filter_item(self, item: dict) -> bool:
        return True

    def map_item(self, item: dict) -> DataItem:
        return DataItem(
            item["text"],
            DataLabel(item["label"]),
            self.source,
        )


def main():
    Importer().run()


if __name__ == "__main__":
    main()
