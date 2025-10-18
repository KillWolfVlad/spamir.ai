from abc import ABC, abstractmethod
from typing import Generator

from spamirai_dataset_common import BaseImporter, DataItem, DataLabel

from .check_users import check_users
from .user_ids_cache import user_ids_cache


class BaseCasImporter(BaseImporter, ABC):
    def __init__(self):
        super().__init__("210_cas")

    @abstractmethod
    def load_user_ids(self) -> Generator[str, None, None]:
        pass

    def load_dataset(self) -> Generator[dict, None, None]:
        buffer_size = 100
        buffered_user_ids = []

        for user_id in self.load_user_ids():
            if len(buffered_user_ids) < buffer_size:
                if user_id not in user_ids_cache:
                    buffered_user_ids.append(user_id)

                continue

            for result in check_users(buffered_user_ids):
                yield result

            user_ids_cache.add_all(buffered_user_ids)
            buffered_user_ids = []

        for result in check_users(buffered_user_ids):
            yield result

        user_ids_cache.add_all(buffered_user_ids)

    def filter_item(self, item: dict) -> bool:
        if not item["ok"] or not item["result"]:
            return False

        result = item["result"]

        if not result["messages"]:
            return False

        return True

    def map_item(self, item: dict) -> Generator[DataItem, None, None]:
        for message in item["result"]["messages"]:
            yield DataItem(message, DataLabel.SPAM, "cas")
