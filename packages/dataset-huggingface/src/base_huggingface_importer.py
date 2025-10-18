from abc import ABC
from typing import Generator

from datasets import load_dataset
from spamirai_dataset_common import BaseImporter


class BaseHuggingFaceImporter(BaseImporter, ABC):
    def __init__(self, hf_dataset_path: str, layer_name: str):
        super().__init__(layer_name)

        self._hf_dataset_path = hf_dataset_path

    @property
    def source(self):
        return f"huggingface-{self._hf_dataset_path}"

    def load_dataset(self) -> Generator[dict, None, None]:
        hf_dataset = load_dataset(self._hf_dataset_path)

        for split in hf_dataset:
            for item in hf_dataset[split]:
                yield item
